import os

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_answer(context, question):

    prompt = f"""
You are PDFMind AI.

Answer the question using ONLY the information available in the uploaded PDF.

If the answer is not available in the provided context, reply exactly:

"I couldn't find that information in the uploaded PDF."

Do not use outside knowledge.
Do not guess.
Keep the answer clear,concise and well formatted.

Context:
{context}

Question:
{question}

Answer:
"""

    try:
        response = model.generate_content(prompt)

        return response.text

    except Exception:
        return "⚠️ Sorry! The AI is temporarily unavailable. Please try again."