str = 'X-DSPAM-Confidence: 0.8475'

# .find() function retrieves index position
ipos = str.find(':')
print(ipos)

# ipos is position 18, str[ipos:] is '18 till the end'
piece = str[ipos+2:]
print(piece, type(piece))


# convert string to float, gets rid of spacing
value = float(piece)
print(value, type(value))

print(value + 42.0)


# Slicing String
s = 'Monty Python'

# sub 0 through 4, at, but not including 4
print(s[0:4])

# 8 thru the end
print(s[8:])

# String Concatentation
a = 'Hello'
b = a + 'There'
print(b)

# add space as separate string, not attached to another word
c = a + ' ' + 'There'
print(c)

# Using in as a logical Operator

fruit = 'banana'

# True
print('n' in fruit)

# use in in conditional
if 'a' in fruit:
    print('Found it!')

# String Library, built into string variables and constants

greet = 'Hello Paul'
zap = greet.lower()
print(zap)

print(greet)

print('Upper Case'.lower())

# find string methods
stuff = 'Hello World'
dir(stuff)

print("upper", stuff.upper())
print("swapcase", stuff.swapcase())
print("rindex of W", stuff.rindex('W'))

e = stuff.endswith
print(e)

c = stuff.count
print(c)

print("find", stuff.find('o'))

# Search and Replace
greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Alice')
print(nstr)

nstr = greet.replace('o', 'X')
print(nstr)

# Prefixes (logical)
line = 'Please have a nice day'
print(line.startswith('Please'))
print("Uppercase P", line.startswith('P'))
print("Lowercase p", line.startswith('p'))

# Parsing and Extracting
data = 'From: George Walker <walker@sgs.tu.ac.th>'
atpos = data.find('@')
print("at position: ", atpos)

sppos = data.find('>', atpos)
print("> position", sppos)

# string slicing
host = data[atpos+1:sppos]
print("institution email:", host)

# Thai characters
thai = 'ไทย'
print("Thai in ไทย", thai)
print(type(thai))

# Summary of Topics:
# string types, read/convert, indexing, slicing, looping strings
# concatenating strings with +
# string library
# comparisons
# searching in strings
# replacing text
# parsing and extracting
