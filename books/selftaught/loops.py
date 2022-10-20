
# split letters from words

name = "Paul"
for l in name:
    print(l)

# print key-values

people = {"G. Bluth II": "Arrested Development",
          "Halpert": "The Office",
          "Galadriel": "Rings of Power"}

for key in people:
    print(key)


# change items in a mutable iterable
tv = ["Sopranos", "Better Call Saul", "Andor"]
i = 0
for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1

print(tv)

# enumerable
tv2 = ["Breaking Bad", "Friends", "Rings of Power"]
for i, show in enumerate(tv2):
    new = tv2[i]
    new = new.upper()
    tv2[i] = new

print(tv2)

# two for-loops
tv3 = ["GOT", "Narcos", "Veep"]
com = ["Seinfeld", "30 Rock", "The Office"]
all_shows = list()

for show in tv3:
    show = show.upper()
    all_shows.append(show)

for show in com:
    show = show.upper()
    all_shows.append(show)

print(all_shows)

# range & break
for i in range(0, 100):
    print
    break


# loop through questions

qs = ["What is your name? ",
      "What is your fav color? ",
      "What is your quest? "]
n = 0
while True:
    print("Type q to quit.")
    a = input(qs[n])
    if a == "q":
        break
    n = (n + 1) % 3

# nested loops

list1 = [1,2,3,4]
list2 = [5,6,7,8]
added = list()
for i in list1:
    for j in list2:
        added.append(i + j)

print(added)