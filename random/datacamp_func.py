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
"""

@check_list
def my_func(value):
    print(value)

try:
    print([1,4,2])
except AssertionError:
    print("Didn't return a list.")

"""

# ---------- Which line of code is missing -----------
from contextlib import contextmanager

@contextmanager
def my_alarm():
    print("Wake up!")
    yield 4
    print("Bye!")

# Create the context manager object
alarm = my_alarm()

# Use the context manager object within the with statement
with alarm as time_left:
    print('{} hours left'.format(time_left))


# ----------- Complete the code (global/ local variables)------

my_str = "ThIs Is a mESsy sTrInG"
def my_function():
    global my_str
    my_str = my_str.lower()
    return my_str

print(my_str)


# -------- Select the code to return the output -----------

def parent_func():
    def child_func(x = 100):
        print(x * 1.08)
    return child_func

output = parent_func()
output(23)

# ------- What is the output of this code ? -----------

import time 
def take_timeout(k=20):
    """Iterates over the list.

    Args:
        k (int): number of iterations
    """
    time.sleep(k)

print(take_timeout.__name__)


# -------- example decorator ---------
def eur_to_dol(func):
    def wrapper(a,b):
        return func(a, b * 1.08)
    return wrapper

@eur_to_dol
def budgeting(a,b):
    print(a*b)

budgeting(20, 34)