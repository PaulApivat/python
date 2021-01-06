# read file
# check length
# open file
# strip white space
# split into words

fname = input('Enter File: ')
if len(fname) < 1:
    fname = 'clown.txt'    # defaults to clown.txt
hand = open(fname)

di = dict()   # create dictionary to count the words

for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        # idiom: retrieve/create/update/counter in one line
        # idiom of using get() to maintain counter for keys in the dictionary
        di[w] = di.get(w, 0) + 1


# print(di)

# Tuples

# x = sorted(di.items())   # tuples can be sorted; this sorts by key
# print(x[:5])                 # list of tuples

# Sort Tuples by Values

tmp = list()
for k, v in di.items():
    newt = (v, k)
    tmp.append(newt)

#print("Flipped", tmp)
tmp = sorted(tmp, reverse=True)
#print("Sorted", tmp[:5])

for v, k in tmp[:5]:
    print(k, v)
