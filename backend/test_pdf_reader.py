from rag.pdf_reader import extract_text

text = extract_text("uploads/A_Review_on_Alzheimers_Disease_Detection_using_Machine_Learning.pdf")

print(text[:500])