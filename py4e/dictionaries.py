# coding: utf-8

lst = list()
lst.append(21)
lst.append(183)
print(lst)

ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)

# The difference is the indexing mechanism
for d in enumerate(ddd):
    print(d)

for l in lst:
    print(l)

for d in ddd.items():
    print(d)

for key, value in ddd.items():
    print(f"key: {key}, value: {value}")

# You can make empty dictionaries using emply curly - diictionary literals
# Common Applications of Dictionaries - making Histograms
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)

ccc['cwen'] = ccc['cwen'] + 1
print(ccc)

# Histogram code
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

# The pattern of checking to see if a key is already in a dictionary and assuming a default value if the key is not there is so common
# The 'get' method for dictionaries
# DICTIONARY IDIOM - how to create new entries and update existing entries
counts = dict()
names = ['paul', 'peter', 'mary', 'mary', 'peter', 'paul', 'paul', 'paul']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

# get a new name that's not in the dictionary, with a default to prevent a traceback
print(counts.get('mike', 0))
