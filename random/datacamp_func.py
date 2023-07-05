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