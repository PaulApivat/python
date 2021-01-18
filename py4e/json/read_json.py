# coding: utf-8

import json

# load json into python, assign to 'data'
with open('your_posts_1.json') as file:
    data = json.load(file)

len(data)  # 2166 dictionaries inside this list

# print first dictionary in 'data' list
for k, v in data[0].items():
    if k == 'data':
        # nested conditional for-loop to get to 'post' content
        for k_i, v_i in v[0].items():
            if k_i == 'post':
                post = v_i
                print(v_i)

post_split = post.split()

# initialize new dictionary to count words
counts = dict()
for word in post_split:
    counts[word] = counts.get(word, 0) + 1
print("\nA count of all the words: \n", counts)

# sort dictionary by keys
sorted_dict = dict()

sorted_keys = sorted(counts, key=counts.get)

for w in sorted_keys:
    sorted_dict[w] = counts[w]
print("\nSorted dictionary: \n", sorted_dict)

print("\nNOW THE FULL DATA\n")
