import fitz
print(fitz.__doc__)

pdf_file = "/home/CE/musaeed/Old Nubian Texts from Gebel.pdf"
doc = fitz.open(pdf_file)

toc = doc.get_toc()
print(f"the toc {toc}")

page_number = 10
page = doc[page_number]  # the short form
print(f"the page number {page_number} is {page}")
text = page.get_text("block")
print(f"the text is {text}")

