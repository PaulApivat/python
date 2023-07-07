import pandas as pd

def add_column(col_name, values, df = None):
    if df is None:
        df = pd.DataFrame()
    df["Tourists"] = ["200", "19", "74"]
    df[col_name] = values
    return df

print(add_column("Arrival", ["199", "20", "73"]))


fruits = ['banana', 'apple']

def shopping_list(item):
    if item in fruits:
        def fruits_price(q, p=1.5):
            return q * p
        return fruits_price
    else:
        print("Unknown item.")

pricing = shopping_list('apple')
print("\n")
print("Price is {}".format(pricing(10)))

# ------------- Writing Functions in Python -------------- #

def multiply(a):
    return a * 10

def subtract(a):
    return a - 10

my_functions = [multiply, subtract, print]

print(my_functions[1](123))

def groceries_list(my_list = []):
    my_list.append("banana")
    return my_list

print("First groceries_list: ", groceries_list())
print("Second groceries_list: ", groceries_list())


"""
def add_hello(func):

    def inner():
        func()
    return inner

@add_hello
def simple(a, b):
    print(a*b)

print(simple(12,34))
"""

x = 32
def my_func():
    z = x
    return z
try:
    print(my_func)
except NameError as e:
    print(e)


# What is the output of this code?
lst = [15, 9, 55, 41, 35, 20, 62, 49]

def compute(value):
    def Average():
        print(sum(value) / len(value))
    return Average

func = compute(lst)
del(lst)
len(func.__closure__)

print(len(func.__closure__))

# What is the output of this code?
def my_function(_list, _int):
    new_int = _int * 10
    _list.append(new_int)
    return _list

l = []
v = 2
print(my_function(l, v))

# What is the output of this code?
@check_list
def my_func(value):
    print(value)

try:
    print([1,4,2])
except AssertionError:
    print("Didn't return a list.")