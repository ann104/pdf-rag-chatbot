from rag.pdf_reader import extract_text
from rag.chunker import chunk_text

# Read the PDF
text = extract_text("uploads/A_Review_on_Alzheimers_Disease_Detection_using_Machine_Learning.pdf")

# Split into chunks
chunks = chunk_text(text)

print("Number of chunks:", len(chunks))

print("\n----------------------\n")

print("First chunk:\n")

print(chunks[0])