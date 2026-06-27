from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

import shutil

from rag.pdf_reader import extract_text
from rag.chunker import chunk_text
from rag.embedder import create_embeddings
from rag.vector_store import store_embeddings
from rag.retriever import retrieve_chunks
from rag.llm import generate_answer

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="../frontend/static"),
    name="static"
)

templates = Jinja2Templates(
    directory="../frontend/templates"
)

# Temporary chat history
# (Later we'll replace this with sessions)
chat_history = []

pdf_uploaded = False
current_pdf = ""
@app.get("/chat")
def chat(request: Request):

    global pdf_uploaded

    if not pdf_uploaded:

        return RedirectResponse(
            "/",
            status_code=303
        )

    return templates.TemplateResponse(
        request=request,
        name="chat.html",
        context={
            "chat_history": chat_history
        }
    )
@app.get("/")
def home(request: Request):

    global chat_history
    chat_history = []

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/upload")
async def upload_pdf(
    request: Request,
    pdf: UploadFile = File(...)
):

    global chat_history
    global pdf_uploaded
    chat_history = []

    file_path = f"uploads/{pdf.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(pdf.file, buffer)

    text = extract_text(file_path)

    chunks = chunk_text(text)

    embeddings = create_embeddings(chunks)

    store_embeddings(chunks, embeddings)
    pdf_uploaded = True
    return templates.TemplateResponse(
        request=request,
        name="chat.html",
        context={
            "chat_history": chat_history
        }
    )


@app.post("/ask")
async def ask_question(
    request: Request,
    question: str = Form(...)
):

    global chat_history

    chunks = retrieve_chunks(question)

    context = "\n\n".join(chunks)

    answer = generate_answer(
    context,
    question
    )

    chat_history.append({
        "question": question,
        "answer": answer
    })

    return templates.TemplateResponse(
        request=request,
        name="chat.html",
        context={
            "chat_history": chat_history
        }
    )

@app.post("/new-chat")
def new_chat():

    global chat_history

    chat_history = []

    return RedirectResponse(
        "/chat",
        status_code=303
    )