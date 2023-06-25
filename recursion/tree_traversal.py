from pprint import pprint
from typing import Mapping, Tuple, Iterator


# nested dictionary
root = {'data': 'A', 'children': [{'data': 'B', 'children': [{'data': 'D', 'children': []}]}, {'data': 'C', 'children': 
[{'data': 'E', 'children': [{'data': 'G', 'children': []},
{'data': 'H', 'children': []}]}, {'data': 'F', 'children': []}]}]}

pprint(root)

def preorderTraverse(node):
    print(node['data'], end=' ') # Access this node's data
    if len(node['children']) > 0:
        # RECURSIVE CASE
        for child in node['children']:
            preorderTraverse(child) # Traverse child nodes
    # BASE CASE
    return

preorderTraverse(root)

def postorderTraverse(node):
    for child in node['children']:
        # RECURSIVE CODE
        postorderTraverse(child) # Traverse child nodes.
    print(node['data'], end=' ') # Access this node's data
    # BASE CASE
    return

print("\n")
print("------- postorderTraverse -------")
postorderTraverse(root)


# another nested dict
D1={1: {2: {3: 4, 5: 6}, 3: {4: 5, 6: 7}}, 2: {3: {4: 5}, 4: {6: 7}}}


def iterdict(node):
    for key, value in node.items():
        if isinstance(value, dict):
            print(key)
            iterdict(value)
        else:
            print(key, ":", value)

print("\n")
print("------- iterdict -------")
iterdict(root)
iterdict(D1)


# Most pythonic and easily understandable
def recursive_items(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield (key, value)
            yield from recursive_items(value)
        else:
            yield (key, value)

print("\n")
print("------- recursive_items on root-------")
for key, value in recursive_items(root):
    print(key, value)

print("\n")
print("------- recursive_items on D1 -------")
for key, value in recursive_items(D1):
    print(key, value)

# from typing import Mapping, Tuple, Iterator

my_dict = {
    "isbn": "123-456-222",
    "author": {"lastname": "Doe", "firstname": "Jane"},
    "editor": {"lastname": "Smith", "firstname": "Jane"},
    "title": "The Ultimate Database Study Guide",
    "category": ["Non-Fiction", "Technology"],
    "first": {
        "second": {"third": {"fourth": {"blah": "yadda"}}},
        "fifth": {"sixth": "seventh"},
    },
}

def traverse_dict(nested: Mapping, parent_key="", keys_to_not_traverse_further=tuple()) -> Iterator[Tuple[str, str]]:
    """Each key is joined with it's parent using dot as a separator.

    Once a `parent_key` matches `keys_to_not_traverse_further`
    it will no longer find its child dicts.
    """
    for key, value in nested.items():
        if isinstance(value, Mapping) and key not in keys_to_not_traverse_further:
            yield from traverse_dict(value, f"{parent_key}.{key}", keys_to_not_traverse_further)
        else:
            yield f"{parent_key}.{key}", value 

print("\n")
print("------- traverse_dict on root -------")
for k, v in traverse_dict(root):
    print(k, v)


print("\n")
print("------- traverse_dict on D1 -------")
for k, v in traverse_dict(D1):
    print(k, v)

print("\n")
print("------- traverse_dict on my_dict -------")
for k, v in traverse_dict(my_dict):
    print(k, v)