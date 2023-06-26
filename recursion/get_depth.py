"""
Three questions to ask of recursive algos:
1. What is the base case? 

leaf node w no children; depth of one level

2. What argument is passed to the recursive function call?

The node whose greatest depth we want to find.

3. Hwo does this argument become closer to the base case? 
"""
from pprint import pprint

root = {'data': 'A', 'children': [{'data': 'B', 'children':
[{'data': 'D', 'children': []}]}, {'data': 'C', 'children':
[{'data': 'E', 'children': [{'data': 'G', 'children': []},
{'data': 'H', 'children': []}]}, {'data': 'F', 'children': []}]}]}

#pprint(root)

def getDepth(node):
    if len(node['children']) == 0:
        # BASE CASE
        return 0
    else:
        # RECURSIVE CASE
        maxChildDepth = 0
        for child in node['children']:
            # Find the depth of each child node:
            childDepth = getDepth(child)
            if childDepth > maxChildDepth:
                # This child is deepest child node found so far:
                maxChildDepth = childDepth
        return maxChildDepth + 1
    
print('Depth of tree is ' + str(getDepth(root)))