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

# Flatten a list (44591 words)
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


def remove_punctuation(words):
    """Remove punctuation from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s]', '', word)
        if new_word != '':
            new_words.append(new_word)
    return new_words

# flat_new_lst4 = remove_punctuation(flat_new_lst3)   - length of flat_new_lst4 < flat_new_lst3    (length: 35640)


def replace_numbers(words):
    """Replace all interger occurrences in list of tokenized words with textual representation"""
    p = inflect.engine()
    new_words = []
    for word in words:
        if word.isdigit():
            new_word = p.number_to_words(word)
            new_words.append(new_word)
        else:
            new_words.append(word)
    return new_words

# flat_new_lst5 = replace_numbers(flat_new_lst4)


nltk.download('stopwords')


def remove_stopwords(words):
    """Remove stop words from list of tokenized words"""
    new_words = []
    for word in words:
        if word not in stopwords.words('english'):
            new_words.append(word)
    return new_words

# flat_new_lst6 = remove_stopwords(flat_new_lst5) -- length flat_new_lst6 < flat_new_lst5 after remove stop words (length: 22675)


def stem_words(words):
    """Stem words in a list of tokenized words"""
    stemmer = LancasterStemmer()
    stems = []
    for word in words:
        stem = stemmer.stem(word)
        stems.append(stem)
    return stems

# flat_new_lst7 = stem_words(flat_new_lst6)


nltk.download('wordnet')


def lemmatize_verbs(words):
    """Lemmatize verbs in a list of tokenized words"""
    lemmatizer = WordNetLemmatizer()
    lemmas = []
    for word in words:
        lemma = lemmatizer.lemmatize(word, pos='v')
        lemmas.append(lemma)
    return lemmas

# flat_new_lst8 = lemmatize_verbs(flat_new_lst7)


def normalize(words):
    words = remove_non_ascii(words)
    words = to_lowercase(words)
    words = remove_punctuation(words)
    words = replace_numbers(words)
    words = remove_stopwords(words)
    return words


words = normalize(flat_new_lst)
print(words)
