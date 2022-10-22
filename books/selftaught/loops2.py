shows = ["the walking dead", "entourage", "the sopranos", "the vampire diaries"]
for s in shows:
    print(s)

for n in range(25,51):
    print(n)

for (i, s) in enumerate(shows, start=1):
    print(i, s)



numbers = ['1','8','7']
n = 0
while True:
    answer = input("Guess the number or type q to quit: ")
    if answer == 'q':
        break 
    elif answer in numbers:
        print("You guessed correctly!")
        break
    else:
        print("Try again!")

# nested loops
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
list3 = list()

for i in list1:
    for j in list2:
        a = i*j
        list3.append(a)

print(list3)