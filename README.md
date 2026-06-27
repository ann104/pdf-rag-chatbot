# 📄 PDFMind AI

### AI-Powered PDF Question Answering System using Retrieval-Augmented Generation (RAG)

PDFMind AI is an intelligent document chatbot that enables users to upload PDF documents and ask questions in natural language. The application retrieves relevant information using semantic search and generates accurate, context-aware answers using Google's Gemini 2.5 Flash model.

---

## ✨ Features

- 📄 Upload PDF documents
- 🤖 AI-powered question answering
- 🔍 Semantic search using vector embeddings
- 🧠 Retrieval-Augmented Generation (RAG)
- ⚡ Fast and accurate responses
- 🔒 Private document processing

---

## 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| Backend | FastAPI |
| Frontend | HTML, CSS |
| AI Model | Google Gemini 2.5 Flash |
| Embedding Model | Sentence Transformers (all-MiniLM-L6-v2) |
| Vector Database | ChromaDB |
| PDF Processing | PyPDF |
| Language | Python |

---

## ⚙️ System Workflow

```text
Upload PDF
      │
      ▼
Extract Text
      │
      ▼
Chunk Text
      │
      ▼
Generate Embeddings
      │
      ▼
Store in ChromaDB
      │
      ▼
User Question
      │
      ▼
Semantic Retrieval
      │
      ▼
Gemini 2.5 Flash
      │
      ▼
AI Response
```

---

## 📂 Project Structure

```text
pdf-rag-chatbot
│
├── backend
│   ├── rag
│   ├── uploads
│   ├── database
│   ├── main.py
│   └── .env
│
├── frontend
│   ├── static
│   └── templates
│
├── requirements.txt
└── README.md
```

---

## 🚀 Future Improvements

- Multi-PDF support
- Persistent chat history
- Authentication
- Cloud deployment
- Mobile responsive UI

---

## 👨‍💻 Author

**Ann Philip**
