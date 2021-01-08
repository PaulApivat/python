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
y = re.findall('[0-9]+', x)    # [0-9]+ is 'any number, one or more numbers'
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

# REGEX Practical Application

# Old way of extracting email

x = 'From paul.apivat@sgs.tu.ac.th Sat Jan 8 09:14:16 2021'
atpos = x.find('@')
print(atpos)  # 16

sppos = x.find(' ', atpos)
print(sppos)  # 29

email = x[atpos+1: sppos]
print(email)


# The Double Split Pattern
words = x.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])


# Regex Version
x = 'From paul.apivat@sgs.tu.ac.th Sat Jan 8 09:14:16 2021'
# search fill find @, then extract [^ ] - not a blank, * is mean of them (greedy)
y = re.findall('@([^ ]*)', x)
print(y)


# Cooler Regex Version (more fine tuned)
x = 'From paul.apivat@sgs.tu.ac.th Sat Jan 8 09:14:16 2021'
# both an IF statement and Regex-extraction
y = re.findall('^From .*@([^ ]*)', x)
print(y)


# Spam Confidence
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    numlist.append(num)
print('Regular:', numlist, '\nMaximum:', max(numlist))


# Escape Character (\)
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x)
print(y)

# SUMMARY
# cryptic but powerful
