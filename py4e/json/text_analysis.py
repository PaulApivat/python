import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
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


# Remove Non-ASCII


def remove_non_ascii(words):
    """Remove non-ASCII character from List of tokenized words"""
    new_words = []
    for word in words:
        new_word = unicodedata.normalize('NFKD', word).encode(
            'ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words

# To LowerCase


def to_lowercase(words):
    """Convert all characters to lowercase from List of tokenized words"""
    new_words = []
    for word in words:
        new_word = word.lower()
        new_words.append(new_word)
    return new_words


# Remove Punctuation , then Re-Plot Frequency Graph

def remove_punctuation(words):
    """Remove punctuation from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s]', '', word)
        if new_word != '':
            new_words.append(new_word)
    return new_words

# Replace Numbers with Textual Representations


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


def remove_stopwords(words):
    """Remove stop words from list of tokenized words"""
    new_words = []
    for word in words:
        if word not in stopwords.words('english'):
            new_words.append(word)
    return new_words


def stem_words(words):
    """Stem words in a list of tokenized words"""
    stemmer = LancasterStemmer()
    stems = []
    for word in words:
        stem = stemmer.stem(word)
        stems.append(stem)
    return stems


def lemmatize_verbs(words):
    """Lemmatize verbs in a list of tokenized words"""
    lemmatizer = WordNetLemmatizer()
    lemmas = []
    for word in words:
        lemma = lemmatizer.lemmatize(word, pos='v')
        lemmas.append(lemma)
    return lemmas


def normalize(words):
    words = remove_non_ascii(words)
    words = to_lowercase(words)
    words = remove_punctuation(words)
    words = replace_numbers(words)
    words = remove_stopwords(words)
    return words


words = normalize(flat_word_token)
print("Length of words list: ", len(words))  # 22676

sents = normalize(flat_sent_token)
print("Length of sentences list: ", len(sents))   # 3194

##### Separate Stems & Lemmatization #####


def stem_and_lemmatize(words):
    stems = stem_words(words)
    lemmas = lemmatize_verbs(words)
    return stems, lemmas


stems, lemmas = stem_and_lemmatize(words)
print('Length of Word Stemmed: \n', len(stems))
print('\nLength of Lemmatized Word:\n', len(lemmas))


##### Part of Speech Tagging #####
# Note: use flat_word_token
# Note: use flat_sent_token


# nltk.download('averaged_perceptron_tagger')

# Sample
# print(nltk.pos_tag(flat_word_token[0:10]))
# print(nltk.pos_tag(flat_sent_token[0:10]))


##### Find Frequency Distribution ######

# Find frequency of words
fdist_word = FreqDist(words)
fdist_word.most_common(50)

# Plot Frequency Graph
fdist_word.plot(50)

# Find frequency of sentence
fdist_sent = FreqDist(sents)
fdist_sent.most_common(10)   # TELLING

# Frequency of (Word) STEMS
fdist_stem_word = FreqDist(stems)
fdist_stem_word.most_common(50)

# Frequency of (Word) LEMMAS
fdist_lemmas_word = FreqDist(lemmas)
fdist_lemmas_word.most_common(50)


### VADER Sentiment Intensity Analyzer ###

# nltk.download('vader_lexicon')

sid = SentimentIntensityAnalyzer()

# for sent in sents[0:10]:
#    sent_scores = sid.polarity_scores(sent)
#    print(sent, sent_scores)
#    print("Type sent", type(sent), "Type sent_scores", type(sent_scores))


# for sent in sents:
#    sent_scores = sid.polarity_scores(sent)
#    df = pd.DataFrame(sent, list(sent_scores.items()), columns=['sentence'])
#    print("Data Frame Shape: ", df.shape)

sentiment = []
sentiment2 = []

for sent in sents:
    sent1 = sent
    sent_scores = sid.polarity_scores(sent1)
    for x, y in sent_scores.items():
        sentiment2.append((x, y))
    sentiment.append((sent1, sent_scores))
    # print(sentiment)

# sentiment
cols = ['sentence', 'numbers']
result = pd.DataFrame(sentiment, columns=cols)
print("First five rows of results: ", result.head())

# sentiment2
cols2 = ['label', 'values']
result2 = pd.DataFrame(sentiment2, columns=cols2)
print("First five rows of results2: ", result2.head())

# len(sentiment)  3194
# len(sentiment2) 12776
# 3194 * 4 = 12776

# result.to_csv('sent_sentiment.csv')
# result2.to_csv('sent_sentiment_2.csv')
