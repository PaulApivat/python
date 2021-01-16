# coding: utf-8
import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in fhand:
    print(line.decode().strip())

# need to have this line a second time for the below nested-loop to work
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()

for line in fhand:
    words = line.decode().split()   # .split() vs .strip() - count words vs letters
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
