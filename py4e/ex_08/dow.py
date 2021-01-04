han = open('mbox-short.txt')

unique = []

for line in han:
    line = line.rstrip()   # strip white space
    wds = line.split()     # split into individual words
    # guardian in a compound statement - first part true, doesn't eval second part
    if len(wds) < 3 or wds[0] != 'From':
        continue
    unique.append(wds[1])
    print(wds[1])  # print email addresses

# use set to delete duplicate emails
unique = set(unique)
print('Unique email addresses:', unique)


# Strings and Lists
line = 'A lot                       of spaces'
etc = line.split()
print(etc)

# specify delimiter to use in splitting
line = 'first;second;third'
semi = line.split(';')
print(semi)
print(len(semi))


# Double Split Pattern
string = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = string.split()
email = words[1]
print(email)

pieces = email.split('@')
print(pieces)

# Summary
# concept of collection (lists)
# lists and for-loops
# indexing and lookup
# list mutability
# functions: len, min, max, sum
# slicing lists
# list methods: append, remove
# sorting lists
# splitting strings into lists of words
# use split to parse strings
