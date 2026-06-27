from rag.pdf_reader import extract_text
from rag.chunker import chunk_text

text = extract_text("uploads/YOURPDF.pdf")

chunks = chunk_text(text)

print("Number of chunks:", len(chunks))

print()

print(chunks[0])