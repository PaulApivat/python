# coding: utf-8

# concatenate list
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b

# slice lists
t = [9, 41, 12, 3, 74, 15]
t[1:3]   # 1 up-to-but-not-including 3
t[:4]
t[3:]
t[:]

x = list()
type(x)
dir(x)  # see all methods associated with list

# Building a list from scratch
stuff = list()
stuff.append('book')
stuff.append(99)
stuff.append('cookie')
print(stuff)

# is something in a list?
some = [1, 9, 21, 10, 16]
9 in some
11 in some
20 not in some

# sort list (changes it)
friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends[1])

# built in functions and lists
nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
sum(nums)

# find the average of a list
print(sum(nums)/len(nums))


# Both while loops do the same thing
total = 0
count = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    total = total + value
    count += 1
average = total / count
print('While Loop one, Average: ', average)


numlist = list()

while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value2 = float(inp)
    numlist.append(value2)
average2 = sum(numlist)/len(numlist)
print('While Loop two, Average: ', average2)
