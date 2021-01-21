import unicodedata
import nltk
import json

# load json into python, assign to 'data'
with open('your_posts_1.json') as file:
    data = json.load(file)

len(data)  # 2166 dictionaries inside this list


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
            count += 1
            print(vee, count)
            #print("this is vee:", vee)
            if len(vee) > 0:
                for k_i, v_i in vee[0].items():  # <-- Bug
                    if k_i == 'post':
                        vee2 = v_i
                    #print("this is vee2:", vee2)
                        empty_lst.append(vee2)

print("This is the empty list:", empty_lst)
print("Length of list: ", len(empty_lst))

# for x,y in enumerate(empty_lst):
#    print(x,y)

# Tokenization (aka Text Segmentation or Lexical Analysis)
nltk.download('punkt')

# Sample tokenization of most recent post
sample_words = nltk.word_tokenize(empty_lst[0])
print(sample_words)

new_lst = [nltk.word_tokenize(sentence) for sentence in empty_lst]
print("Non-Flatten list: ", new_lst)

#new_lst2 = []
# for sentence in empty_lst:
#    new_lst2.append(nltk.word_tokenize(sentence))

# Flatten a list
flat_new_lst = [item for sublist in new_lst for item in sublist]
print("Flatten list: ", len(flat_new_lst))


# Initialize New Dictionary to Count Words
counts = dict()

for word in flat_new_lst:
    counts[word] = counts.get(word, 0) + 1
print("\nA count of all the words: \n", counts)

# Sort dictionary by keys
sorted_dict = dict()

sorted_keys = sorted(counts, key=counts.get)

for w in sorted_keys:
    sorted_dict[w] = counts[w]
print("\nSorted dictionary: \n", sorted_dict)

# Normalization needs to be done on a list
# source: https://www.kdnuggets.com/2018/03/text-data-preprocessing-walkthrough-python.html


# use 'flat_new_lst' (List) instead of 'sorted_dict' (Dictionary)
# The TIS-620 (Thai Industrial Standard 620-2533) is structured Extended ASCII, full compatibility w 7-bit ASCII


def remove_non_ascii(words):
    """Remove non-ASCII character from List of tokenized words"""
    new_words = []
    for word in words:
        new_word = unicodedata.normalize('NFKD', word).encode(
            'ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words

# flat_new_lst2 = remove_non_ascii(flat_new_lst)


def to_lowercase(words):
    """Convert all characters to lowercase from List of tokenized words"""
    new_words = []
    for word in words:
        new_word = word.lower()
        new_words.append(new_word)
    return new_words

# flat_new_lst3 = to_lowercase(flat_new_lst2)
