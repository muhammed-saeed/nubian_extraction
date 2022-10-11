import fitz
print(fitz.__doc__)
filename = r"C:\Users\lst\Desktop\Old Nubian Dataset\The old nubian language.pdf"
nubi_file = r"C:\Users\lst\Desktop\vocabulary\dataset\nubi_file.nubi"
english_file = r"C:\Users\lst\Desktop\vocabulary\dataset\en_file.en"
keywords = ["Transliteration", "Translations", "Glossary"]
doc = fitz.open(filename)     # or fitz.Document(filename)
print(doc.page_count)
pages = []
for page in range(59,67):
    a = doc.load_page(page)
    text = a.get_text("blocks")
    pages.append(text)
    # print(pages)

print(len(pages))
nubi_lines = []
nubian_starting_pages = [0,1,2,3]
nubian_starting_blocks = [4,1,1,1]
for index, page in enumerate(nubian_starting_pages):
    text = pages[page]
    print(type(text))
    nubi_lines.extend(text[nubian_starting_blocks[index]][4:-2])
# print(nubi_lines)
print(pages[3][1])

print("##############################")
print("##############################")
print("##############################")
english_starting_pages = [3,4,5,6]
english_starting_blocks = [4,1,1,1]
english_lines = []
for index, page in enumerate(english_starting_pages):
    text = pages[page]
    print(type(text))
    english_lines.extend(text[english_starting_blocks[index]][4:-2])
# print(english_lines)

with open(nubi_file, "w", encoding="utf-8") as fb:
    fb.writelines(nubi_lines)

with open(english_file, "w", encoding="utf-8") as fb:
    fb.writelines(english_lines)
# print(" ".join(pages))

# print(pages)

# blocks = a.get_text("dict")["blocks"][1:]

