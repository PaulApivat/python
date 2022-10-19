
def square():
    a = input("type a number: ")
    a = int(a)
    return a * a
    
#result = square()
#print("\n" + "your number squared is: ", result)

def print_string():
    a = input("type a word: ")
    print(a)

#result2 = print_string()
#result2

# three required, two optional params
def add_params(a, b, c, d = 1, e = 2):
    return a + b + c + d + e

#result3 = add_params(1,2,3,4,5)
#print(result3)

def divide(a):
    b = int(a/2)
    return b

result4 = divide(10)

def multiply(a):
    b = a * 4
    return b

result5 = multiply(result4)
print(result5)

def convert_string():
    a = input("type a number: ")
    a = float(a)
    try:
        a / (a - int(a))
        print("great job, that's a float")
    except ZeroDivisionError:
        raise Exception("Must be a float")
    

result6 = convert_string()
result6