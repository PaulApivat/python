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