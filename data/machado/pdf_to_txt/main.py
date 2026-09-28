import os 
from pypdf import PdfReader

def convert_pdf_to_txt(dst_path: str = None):
    if dst_path is None:
        dst_path = os.path.join(os.path.dirname(__file__), 'input.txt')

    pdf_dir = os.path.join(os.path.dirname(__file__), 'input')

    with open(dst_path, 'w', encoding='utf-8') as output_file:
        for filename in os.listdir(pdf_dir):
            if filename.endswith('.pdf'):
                print(f"Converting {filename} to text...")
                pdf_path = os.path.join(pdf_dir, filename)
                reader = PdfReader(pdf_path)
                text = ''
                for num, page in enumerate(reader.pages, start=1):
                    if num <= 2: # ignora as duas primeiras páginas 
                        continue

                    if num == len(reader.pages) - 2: # ignora as duas últimas páginas
                        break

                    text += page.extract_text() + '\n'
                output_file.write("\n".join(line.lstrip(" \t") for line in text.split("\n")) + "\n")
                print(f"Converted {filename} to text.")
    