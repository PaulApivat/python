
# The 'problems' parameter is a list of strings
# If there are too many problems supplied to function (>5) return "error: too many problems"

# The appropriate operators the function will accept are *addition* and *subtraction*.
# Multiplication/Division will return an error - - use any()
# source: https://stackoverflow.com/questions/3389574/check-if-multiple-strings-exist-in-another-string
# loop through list, then for each item, split(), if each item contains "x" OR "/", then return error
# Error: Operator must be '+' or '-'.


# use .split() to split string into parts

# resources:
# https://stackoverflow.com/questions/16335771/shorter-way-to-check-if-a-string-is-not-isdigit
# https://stackoverflow.com/questions/21388541/how-do-you-check-in-python-whether-a-string-contains-only-numbers/21388567


# problematic list
prob_list = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "1 + 38398"]
prob_list_2 = ["32 + 698", "3801 - 2", "45 + 43", "1 x 3"]
prob_list_3 = ["32 + 698", "3801 - 2", "45 + 43", "1 / 3"]
problems = ["32 / 698", "3801 - 2", "45 + 4?3", "123 + 49", "1 + 345673"]


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
        # short way to check if string is not isdigit()
        elif(not split_prob[0].isdigit() or not split_prob[2].isdigit()):
            print("Error: Numbers must only contain digits.")
        # prevent TypeError: '<' not supported between instances of 'str' and 'int'
        elif(int(split_prob[0]) > 4 or int(split_prob[2]) > 4):
            print("Error: Numbers cannot be more than four digits.")
        else:
            continue

    print("Continue. Fine.")

    arranged_problems = ["Initial check passed."]

    return arranged_problems

# Re-Formatting Math Problems


lst = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]


# v2.1
for s in lst:
    split_s = s.split()
    top = split_s[0]
    bottom = split_s[2]
    operator = split_s[1]
    if(len(top) > len(bottom)):
        line = "-" * (len(top) + 2)
    else:
        line = "-" * (len(bottom) + 2)
    output = [f"{top:>{len(line) + 1 }}", '\n', operator,
              f"{bottom:>{len(line) - 2 }}", '\n', line, '\n']
    output2 = ' '.join(output)
    print(output2)


# v2.2
for s in lst:
    split_s = s.split()
    top = split_s[0]
    bottom = split_s[2]
    operator = split_s[1]
    if(len(top) > len(bottom)):
        line = "-" * (len(top) + 2)
    else:
        line = "-" * (len(bottom) + 2)
    output = [f"{top:>{len(line) + 1 }}", '\n', operator,
              f"{bottom:>{len(line) - 2 }}", '\n', line, '\n']
    print(' '.join([x for x in output]), end='')

    # Different Options to print output
    print(output)  # four lists printed vertically
    print(output, end='')  # four lists printed horizontally
    print(*output)  # four lists, joined, printed vertically
    print(*output, end='')  # same as above, remove last '\n'
    print(' '.join(output))  # same as above
    print(' '.join(output), end='')  # same
    print(' '.join([x for x in output]))  # same
    print(' '.join([x for x in output]), end='')  # same
