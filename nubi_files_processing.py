import re
english_file = r"C:\Users\lst\Documents\nubian_extraction\dataset\en_file.en"
nubi_file = renglish_file = r"C:\Users\lst\Documents\nubian_extraction\dataset\nubi_file.nubi"

def process_file(nubi_text):
    no_numbers = re.split('\d+', nubi_text)
    no_numbers_string = " ".join(no_numbers)
    no_dot = no_numbers_string.split('.')
    return no_dot
nubi_text = open(nubi_file, encoding="utf-8").read()
nubi_clean = process_file(nubi_text)
en_text = open(english_file, encoding="utf-8").read()
en_clean = process_file(en_text)
print(nubi_text)
print("######################")
print(nubi_clean)
print(len(nubi_clean))
print(len(en_clean))
# with open(nubi_file, "w", encoding="utf-8") as fb:
#     fb.writelines(nubi_clean)
# with open(english_file, "w", encoding="utf-8") as fb:
#     fb.writelines(en_clean)





