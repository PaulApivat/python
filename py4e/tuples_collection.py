# coding: utf-8
# Tuples are like lists
# Tuples are immutable (unlike lists)

x = [9, 8, 7]
x[2] = 6
print(x)

y = 'ABC'
type(y)
y[2] = 'D'    # TypeError, strings immutable

z = (5, 4, 3)
z[2] = 0      # TypeError, tuples immutable

# Immutability means more efficient, less storage space, quicker to access (unlike lists)

# Things not to do with tuples
x = (3, 2, 1)
x.sort()     # 'tuple' object has no attribute 'sort'
x.append(5)  # 'tuple' object has no attribute 'append'

# When making 'temporary variables', we tend to use tuples

# Tuples and Assignment

# Tuples left hand side
(x, y) = (4, 'fred')

# The items() method in Dictionaries returns a list of key-value TUPLES
d = dict()
d['quincy'] = 1
d['beau'] = 5
d['kris'] = 9
for (k, i) in d.items():
    print(k, i)

tups = d.items()
print(tups)

# TUples are Comparable (left to right)
# ONly scan until it has a definitive answer
(0, 1, 2) < (5, 1, 2)                       # True
(0, 1, 200) < (0, 3, 4)                 # True
(0, 1, 200) < (0, 0.5, 2000)            # False
('Jones', 'Sally') > ('Adams', 'Sam')   # True
