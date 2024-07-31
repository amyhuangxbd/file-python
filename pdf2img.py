import fitz  # PyMuPDF
from PIL import Image
import io

def pdf_to_images(pdf_path, output_folder):
    pdf_document = fitz.open(pdf_path)
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap()
        img = Image.open(io.BytesIO(pix.tobytes()))
        img.save(f"{output_folder}/page_{page_num + 1}.png")
    print(f"PDF 转换完成，总共 {len(pdf_document)} 页")

pdf_path = './example.pdf'
output_folder = 'output_images'
pdf_to_images(pdf_path, output_folder)
