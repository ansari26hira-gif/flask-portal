import fitz # PyMuPDF
import os

def read_pdf_text(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except:
        return ""

def rag_search(question, folder="uploads"):
    all_text = ""
    files_found = []
    for file in os.listdir(folder):
        if file.endswith(".pdf") or file.endswith(".xlsx"):
            path = os.path.join(folder, file)
            if file.endswith(".pdf"):
                all_text += read_pdf_text(path) + "\n"
                files_found.append(file)

    # Simple RAG: keyword matching
    question_lower = question.lower()
    relevant = []
    for line in all_text.split("\n"):
        if any(word in line.lower() for word in question_lower.split()):
            if line.strip():
                relevant.append(line.strip())

    if not relevant:
        return f"Maaf karo, '{question}' ka jawab aapke uploaded files me nahi mila. Files: {files_found}"

    answer = f"Answer from your files ({', '.join(files_found)}):\n\n"
    answer += "\n".join(relevant[:5]) # top 5 lines
    return answer