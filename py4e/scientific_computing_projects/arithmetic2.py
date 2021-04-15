import operator

print("arithmetic2.py running...")

# Test in order

lst = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
problems = ["32 / 698", "3801 - 2", "45 + 4?3", "123 + 49", "1 + 345673"]


def is_correct_format(problems):
    if len(problems) > 5:
        print('Error: Too many problems.')
    else:
        for item in problems:
            problem = item.split(' ')
            wrong_operator = ['x', '/']

            if (not problem[0].isdigit() or not problem[2].isdigit()):
                print("Error: Numbers must only contain digits.")
                correct_format = False
                print("problematic equation: ", problem)

            elif any(x in problem for x in wrong_operator):
                print("Error: Operator must be '+' or '-'.")
                correct_format = False
                print("problematic equation: ", problem)

            elif max(len(problem[0]), len(problem[2])) > 4:
                print("Error: Numbers cannot be more than four digits.")
                correct_format = False
                print("problematic equation: ", problem)

            else:
                correct_format = True

        return correct_format
