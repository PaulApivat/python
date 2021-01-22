from nltk.stem import LancasterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import re
import unicodedata
import nltk
import json
import inflect
import matplotlib.pyplot as plt

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

##### Sample Tokenizations ######

# sample_words = nltk.word_tokenize(empty_lst[0])        len: 96
# sample_sentence = nltk.sent_tokenize(empty_lst[0])     len: 5

##### Tokenize Facebook Posts #####

# - list of list, len: 1762 (each list contain individual words)
nested_word_token = [nltk.word_tokenize(word) for word in empty_lst]

# - list of list, len: 1762 (each list contain sentences)
nested_sent_token = [nltk.sent_tokenize(lst) for lst in empty_lst]

print("Nested Word Tokens: ", len(nested_word_token))
print("Nested Sentence Token: ", len(nested_sent_token))

### FLATTEN LIST ###

flat_word_token = [item for sublist in nested_word_token for item in sublist]
print("Flatten word token: ", len(flat_word_token))

flat_sent_token = [item for sublist in nested_sent_token for item in sublist]
print("Flatten sentence token: ", len(flat_sent_token))

# Find Frequency Distribution

# Find frequency of words
fdist_word = FreqDist(flat_word_token)

# Find frequency of sentence
fdist_sent = FreqDist(flat_sent_token)

# fdist_word.most_common(50)

# Plot Frequency Graph

# fdist_word.plot(50)
# fdist_sent.most_common(10)
