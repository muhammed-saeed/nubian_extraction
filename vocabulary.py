english_dictionary_path = r"C:\Users\lst\Desktop\vocab_pcm_en.tokenized.pcm-en\dict.en.txt"
pcm_dictionary_path = r"C:\Users\lst\Desktop\vocab_pcm_en.tokenized.pcm-en\dict.pcm.txt"
#windows_path = "C:\Users\lst\Desktop\vocab_pcm_en.tokenized.pcm-en"
english_data = open(english_dictionary_path,"r", encoding="utf-8").readlines()
pcm_data = open(pcm_dictionary_path, "r",encoding="utf-8").readlines()
pcm_keys=[]
en_keys = []
pcm_values = []
en_values = []
for index, element in enumerate(pcm_data):
    pcm_data[index] = pcm_data[index].strip().split(" ")
    pcm_data[index][1] = int(pcm_data[index][1])
    element = pcm_data[index][0].lower()
    if element not in pcm_keys:
        pcm_keys.append(element)
        pcm_values.append(pcm_data[index][1])
    else:
        ind = pcm_keys.index(element)
        pcm_values[ind] += pcm_data[index][1]
    

    
for index, element in enumerate(english_data):
    english_data[index] = english_data[index].strip().split(" ")
    english_data[index][1] = int(english_data[index][1])
    element = english_data[index][0].lower()
    if element not in en_keys:
        en_keys.append(element)
        en_values.append(english_data[index][1])
    else:
        ind = en_keys.index(element)
        en_values[ind] += english_data[index][1]

print(en_keys[0])
print(en_values[0])

top_k = 5
english_to_pcm_overlap = {}
pcm_to_english_overlap = {}
pcm_none = []
en_top_k = []
pcm_top_k = []

en_percentage = []
for index in range(top_k):
    en_key = en_keys[index]
    en_top_k.append(en_keys[index])
    try:
        ind = pcm_keys.index(en_key)
        english_to_pcm_overlap[en_values[index]] = pcm_values[ind]
        en_percentage.append(float(en_values[index]/pcm_values[ind]))
    except:
        ind = None
        english_to_pcm_overlap[pcm_values[index]] = 0
        en_values.append(en_key)


print(english_to_pcm_overlap)
print(en_top_k)

for index in range(top_k):
    pcm_key = pcm_keys[index]
    pcm_top_k.append(pcm_key)
    try:
        ind = en_keys.index(pcm_key)
        pcm_to_english_overlap[pcm_values[index]] = en_values[ind]
    except:
        ind = None
        pcm_to_english_overlap[pcm_values[index]] = 0
        pcm_none.append(pcm_key)
    # pcm_to_english_overlap[pcm_values[index]] = en_values[ind]

print(pcm_to_english_overlap)
print(pcm_none)
print(pcm_top_k)

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
langs = pcm_top_k
students = [23,17,35,29,12]
ax.bar(langs,students)
# plt.set_title("EN to PCM overlap ")
plt.plot()

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
langs = en_top_k
students = [23,17,35,29,12]
ax.bar(langs,students)
# plt.set_title("PCM to EN overlap")
plt.plot()
plt.show()





    

