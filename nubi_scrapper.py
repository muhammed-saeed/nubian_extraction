import fitz
import re
print(fitz.__doc__)

def remove_new_lines(nubi_lines):
    cleaned = []
    for line in nubi_lines:
        cleaned.append(line.strip())
    text = " ".join(cleaned)
    text_2 = text.replace("\n", " ")
    return text_2

def process_file(nubi_text):
    no_numbers = re.sub('\d+.', "\n" ,nubi_text)
    # no_numbers_string = " ".join(no_numbers)
    # no_dot = no_numbers_string.split('.')
    no_numbers  = no_numbers.split("\n")

    for index, line in enumerate(no_numbers):
        no_numbers[index] = line.strip()
    
    return no_numbers



filename = r"C:\Users\lst\Desktop\Old Nubian Dataset\The old nubian language.pdf"
nubi_file = r"C:\Users\lst\Documents\nubian_extraction\dataset\nubi_file.nubi"
english_file = r"C:\Users\lst\Documents\nubian_extraction\dataset\en_file.en"
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

print(nubi_lines[0][0])

english_lines[0] = english_lines[0].replace("o", "0", 1)
nubi_lines[0] = nubi_lines[0].replace("o", "0", 1)
print(nubi_lines[0][0])

# print(cleaned_text)
print("######################")
print("######################")
# print(nubi_splitted_text)


cleaned_text = remove_new_lines(nubi_lines)
nubi_splitted_text = process_file(cleaned_text)


en_cleaned_text = remove_new_lines(english_lines)
en_splitted_text = process_file(en_cleaned_text) 


with open(nubi_file, "w", encoding="utf-8") as fb:
    fb.writelines(nubi_lines)

with open(english_file, "w", encoding="utf-8") as fb:
    fb.writelines(english_lines)
# print(" ".join(pages))


clean_nubi_file = r"C:\Users\lst\Documents\nubian_extraction\clean_dataset\nubi_clean.txt"
clean_en_file = r"C:\Users\lst\Documents\nubian_extraction\clean_dataset\en_clean.txt"

with open(clean_nubi_file, "w", encoding="utf-8") as fb:
    for line in nubi_splitted_text:
        fb.write(line)
        fb.write("\n")
with open(clean_en_file, "w", encoding="utf-8") as fb:
    for line in en_splitted_text:
        fb.write(line)
        fb.write("\n")

# print(pages)

# blocks = a.get_text("dict")["blocks"][1:]

