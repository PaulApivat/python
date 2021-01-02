
fh = open('mbox-short.txt')
print(fh)

for lx in fh:
    ly = lx.rstrip()   # get rid of \n
    print(ly.upper())  # print all lines as uppercase
