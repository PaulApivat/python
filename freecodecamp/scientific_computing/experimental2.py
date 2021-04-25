from collections import OrderedDict

import operator

print("experimental2.py running...")

# Test in order

lst = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
problems = ["32 / 698", "3801 - 2", "45 + 4?3", "123 + 49", "1 + 345673"]


def is_correct_format(problems):
    error = ' '
    correct_format = True
    if len(problems) > 5:
        error = 'Error: Too many problems.'
        correct_format = False
    else:
        for item in problems:
            problem = item.split(' ')
            wrong_operator = ['x', '/']

            if (not problem[0].isdigit() or not problem[2].isdigit()):
                error = "Error: Numbers must only contain digits."
                correct_format = False
                break

            elif any(x in problem for x in wrong_operator):
                error = "Error: Operator must be '+' or '-'."
                correct_format = False
                break

            elif max(len(problem[0]), len(problem[2])) > 4:
                error = "Error: Numbers cannot be more than four digits."
                correct_format = False
                break
            else:
                correct_format = True

        return {"correct_format": correct_format, "error": error}


def arithmetic_arranger(problems, solve=False):
    if is_correct_format(problems):
        arranged_problems = ""
        dict = {"+": operator.add, "-": operator.sub}
        first = [*range(len(problems))]
        op = [*range(len(problems))]
        second = [*range(len(problems))]
        x = 0
        for prob in problems:
            first[x], op[x], second[x] = prob.split()
            x += 1
        # first line
        for i in range(len(problems)):
            len_first = len(str(int(first[i])))
            len_second = len(str(int(second[i])))
            if len_first > len_second:
                arranged_problems += str(" " * (len_first -
                                                len_first + 2) + first[i] + " "*4)
            else:
                arranged_problems += str(" " * (len_second -
                                                len_first + 2) + first[i] + " "*4)

        arranged_problems = arranged_problems[:-4]
        arranged_problems += str("\n")

        # second line
        for i in range(len(problems)):
            len_first = len(str(int(first[i])))
            len_second = len(str(int(second[i])))
            if len_first > len_second:
                arranged_problems += str(op[i] + " " * (
                    len_first - len_second + 1) + second[i] + " "*4)
            else:
                arranged_problems += str(op[i] + " " * (
                    len_second - len_second + 1) + second[i] + " "*4)

        arranged_problems = arranged_problems[:-4]
        arranged_problems += str("\n")

        # third line
        for i in range(len(problems)):
            len_first = len(str(int(first[i])))
            len_second = len(str(int(second[i])))
            if len_first > len_second:
                arranged_problems += str("--" + "-" * len_first + "    ")
            else:
                arranged_problems += str("--" + "-" * len_second + "    ")

        arranged_problems = arranged_problems[:-4]
        arranged_problems += str("\n")

        # solve parameter
        if solve:
            total = [*range(len(problems))]
            x = 0
            for i in range(len(problems)):
                total[x] = dict[op[i]](int(first[i]), int(second[i]))
                len_first = len(str(int(first[i])))
                len_second = len(str(int(second[i])))
                if len_first > len_second:
                    arranged_problems += str(" " * (len_first -
                                                    len(str(total[x])) + 2) + str(total[x]) + "    ")
                else:
                    arranged_problems += str(" " * (len_second -
                                                    len(str(total[x])) + 2) + str(total[x]) + "    ")
                x += 1
            arranged_problems = arranged_problems[:-4]

        return arranged_problems
