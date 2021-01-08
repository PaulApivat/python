# Regex Quick Guide

# ^     Matches the beginning of a line
# $     Matches the end of a line
# .     Matches any character
# \s    Matches whitespace
# \S    Matches any non-whitespace character
# *     Repeats a character zero or more times (greedy)
# *?    Repeats a character zero or more times (non-greedy)
# +     Repeats a character one or more times (greedy)
# +?    Repeats a character one or more times (non-greedy)
# [aeiou]   Matches a single character in the listed set
# [^XYZ]    Matches a single character not in the listed set
# [a-z0-9]  The set of characters can include a range
# (         Indicates where string extraction is to start
# )         Indicates where string extraction is to end

import re

# Using re.search() like startswith()

print('first function')
hand = open('clown.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^the', line):
        print(line)

print('second function')
hand = open('clown.txt')
for line in hand:
    line = line.strip()
    if line.startswith('the'):
        print(line)

# Matching and Extracting
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)    # [0-9]+ is 'one or more numbers'
print(y)

v = re.findall('[aeiou]+', x)
print(v)

# Warning: Greedy Matching
x = 'From: Using the : character'
y = re.findall('^F.+:', x)      # First character in the match is an F
# + is one or more charadcter
# Last character in the match is :
print(y)

# Non-Greedy Matching (add ?)
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)     # add ? to be non-greedy
print(y)


# Fine-Tuning String Extraction
x = 'From paul.apivat@gmail.com Sat Jan 8 09:14:16 2008'
# none-whitepsace char, greedy, @-sign, none-whitespace, greedy
y = re.findall('\S+@\S+', x)
print(y)

# Fine-tuning using From
x = 'From paul.apivat@gmail.com Sat Jan 8 09:14:16 2008'
y = re.findall('^From (\S+@\S+)', x)
print(y)
