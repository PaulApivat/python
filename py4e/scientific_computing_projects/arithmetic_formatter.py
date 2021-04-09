
# The 'problems' parameter is a list of strings
# If there are too many problems supplied to function (>5) return "error: too many problems"

# The appropriate operators the function will accept are *addition* and *subtraction*.
# Multiplication/Division will return an error - - use any()
# source: https://stackoverflow.com/questions/3389574/check-if-multiple-strings-exist-in-another-string
# loop through list, then for each item, split(), if each item contains "x" OR "/", then return error
# Error: Operator must be '+' or '-'.


# use .split() to split string into parts

# problematic list
prob_list = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "1 + 3"]
prob_list_2 = ["32 + 698", "3801 - 2", "45 + 43", "1 x 3"]
prob_list_3 = ["32 + 698", "3801 - 2", "45 + 43", "1 / 3"]


def arithmetic_arranger(problems):

    if(len(problems) > 4):
        print("Error: Too many problems.")

    """check for inappropriate operators: x or / """
    """check numbers only contain digits"""
    """check if numbers more than four digits"""

    for item in problems:
        split_prob = item.split()
        matches = ['x', '/']
        if any(x in split_prob for x in matches):
            print("Error: Operator must be '+' or '-'.")
        elif(not split_prob[0].isdigit() or not split_prob[2].isdigit()):
            print("Error: Numbers must only contain digits.")
        elif(int(split_prob[0]) > 4 or int(split_prob[2]) > 4):
            print("Error: Numbers cannot be more than four digits.")
        else:
            continue

    print("Continue. Fine.")

    arranged_problems = ["Initial check passed."]

    return arranged_problems
