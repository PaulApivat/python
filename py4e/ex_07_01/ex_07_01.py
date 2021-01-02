
fh = open('mbox-short.txt')
print(fh)   # print out file handler (not content of file)

# count lines in file
count = 0

# print out content of file, line-by-line
for lx in fh:
    count += 1
    ly = lx.rstrip()   # get rid of \n
    print(ly.upper())  # print all lines as uppercase
print('Line Count:', count)


# reading *whole* file
fhand = open('mbox-short.txt')

inp = fhand.read()

print("Number of characters:", len(inp))
print("Print first twenty characters:", inp[:20])


# Search through a File

fhand = open('mbox-short.txt')

for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)


# Search through a file (alternative pattern with *continue*)

fhand = open('mbox-short.txt')

print("\nAlternative pattern:")

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)


# Using in to select lines (skipping)

print("\nPrint all line that have uct.ac.za\n")

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)

# Prompt for File Name
# then take input from user and figure something about the txt file

print("\nPrompt for file name from user\n")

fname = input('Enter the file name: ')

# to prevent user from writing incorrect file names
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count += 1
print('There were', count, 'subject lines in', fname)

# Summary

# secondary storage
# open file - file handle
# file structure - newline or \n
# read file line-by-line with for-loop
# searching for specific lines
# reading file names
# dealing with incorrect file
