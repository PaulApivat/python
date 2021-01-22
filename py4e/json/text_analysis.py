from nltk.stem import LancasterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
import re
import unicodedata
import nltk
import json
import inflect

# load json into python, assign to 'data'
with open('your_posts_1.json') as file:
    data = json.load(file)

print("data is a: ", type(data))
print("Length of data: ", len(data))

# create empty list
empty_lst = []

# create counter
count = 0

# multiple nested loops to store all post in empty list
for dct in data:
    for k, v in dct.items():
        if k == 'data':
            vee = v
            # helping to diagnose a problem (line 233), empty list
            #count += 1
            #print(vee, count)
            #print("this is vee:", vee)
            if len(vee) > 0:
                for k_i, v_i in vee[0].items():  # <-- Bug
                    if k_i == 'post':
                        vee2 = v_i
                    #print("this is vee2:", vee2)
                        empty_lst.append(vee2)

print("This is the empty list: ", empty_lst)
print("\nLength of list: ", len(empty_lst))

# Sample Tokenizations
# sample_words = nltk.word_tokenize(empty_lst[0])        len: 96
# sample_sentence = nltk.sent_tokenize(empty_lst[0])     len: 5
