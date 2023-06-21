from pprint import pprint


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