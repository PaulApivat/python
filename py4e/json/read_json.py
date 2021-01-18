# coding: utf-8

import json

# load json into python, assign to 'data'
with open('your_posts_1.json') as file:
    data = json.load(file)

# print first dictionary in 'data' list
for k, v in data[0].items():
    if k == 'data':
        # nested conditional for-loop to get to 'post' content
        for k_i, v_i in v[0].items():
            if k_i == 'post':
                print(v_i)
