import fitz
print(fitz.__doc__)
filename = r"C:\Users\lst\Desktop\Old Nubian Dataset\The old nubian language.pdf"
keywords = ["Transliteration", "Translations", "Glossary"]
doc = fitz.open(filename)     # or fitz.Document(filename)
print(doc.page_count)
pages = []

a = doc.load_page(59)
text = a.get_text("text")
pages.append(text)
print(pages[0])


print("##############################")
print("##############################")
print("##############################")


# blocks = a.get_text("dict")["blocks"][1:]


a = doc.load_page(60)
text = a.get_text("text")
pages.append(text)
print(pages[1])

# for page in range(60,67):

#     a = doc.load_page(page)
#     text = a.get_text("blocks")
#     pages.append(text)
# print(pages)