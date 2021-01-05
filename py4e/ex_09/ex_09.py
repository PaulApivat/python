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
        di[w] = di.get(w, 0) + 1


#print(di)

# now we want to  find the most common word

largest = -1
theword = None

for key, value in di.items():
    #print(key,value)
    if value > largest:
        largest = value
        theword = key

print('The largest word is:', theword, largest)