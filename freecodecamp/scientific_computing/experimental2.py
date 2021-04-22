from collections import OrderedDict

import operator

print("experimental2.py running...")

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


def arithmetic_arranger(problems, solve=False):
    if is_correct_format(problems):
        # arranged_problems = ""
        dict = {"+": operator.add, "-": operator.sub}
        for prob in problems:
            prob_split = prob.split()
            first = prob_split[0]
            second = prob_split[2]
            sign = prob_split[1]
            if(len(first) > len(second)):
                line = "-" * (len(first) + 2)
            else:
                line = "-" * (len(second) + 2)
            arranged_problems = [f"{first:>{len(line) + 1 }}", '\n', sign,
                                 f"{second:>{len(line) - 2 }}", '\n', line, '\n']

        return print(' '.join(arranged_problems))


def arithmetic_arranger2(problems, solve=False):
    if is_correct_format(problems):
        arranged_problems = ""
        dict = {"+": operator.add, "-": operator.sub}
        first = [*range(len(problems))]
        second = [*range(len(problems))]
        sign = [*range(len(problems))]
        x = 0
        for i in problems:
            first[x], sign[x], second[x] = i.split()
            x += 1
        # each line
        for prob in problems:
            prob_split = prob.split()
            first = prob_split[0]
            second = prob_split[2]
            sign = prob_split[1]
            line = str(
                "--" + "-" * (len(str(max(int(first), int(second))))) + "")

            arranged = [f"{first:>{len(line) + 1 }}", '\n', sign,
                        f"{second:>{len(line) - 2 }}", '\n', line, '\n']
            #print(' '.join(arranged))

            arranged_problems += ' '.join(arranged) + '\n'

        return arranged_problems


print(arithmetic_arranger2(lst))

# arithmetic_arranger3


def arithmetic_arranger3(problems, solve=False):
    if is_correct_format(problems):
        arranged_problems = ""
        dict = {"+": operator.add, "-": operator.sub}
        first = [*range(len(problems))]
        second = [*range(len(problems))]
        sign = [*range(len(problems))]
        x = 0
        for i in problems:
            first[x], sign[x], second[x] = i.split()
            x += 1
        # each line
        # first line
        for i in range(len(problems)):
            arranged_problems += str(" " * (len(str(max(int(first[i]), int(second[i])))) - len(
                str(first[i])) + 2) + first[i] + " "*4)

        arranged_problems += str("\n")

        # second line
        for i in range(len(problems)):
            arranged_problems += str(sign[i] + " " * (len(str(max(int(first[i]), int(second[i])))) - len(
                str(second[i])) + 1) + second[i] + " "*4)

        arranged_problems += str("\n")

        # third line
        for i in range(len(problems)):
            arranged_problems += str("--" + "-" *
                                     (len(str(max(int(first[i]), int(second[i]))))) + "    ")

        arranged_problems += str("\n")

        if solve:
            total = [*range(len(problems))]
            x = 0
            for i in range(len(problems)):
                total[x] = dict[sign[i]](int(first[i]), int(second[i]))
                arranged_problems += str(" " * (len(str(max(int(first[i]), int(second[i])))) - len(
                    str(total[x])) + 2) + str(total[x]) + "    ")
                x += 1

        return arranged_problems


# arithmetic_arranger4

def arithmetic_arranger4(problems, solve=False):
    if is_correct_format(problems):
        arranged_problems = ""
        dict = {"+": operator.add, "-": operator.sub}
        first = [*range(len(problems))]
        second = [*range(len(problems))]
        sign = [*range(len(problems))]
        x = 0
        for i in problems:
            first[x], sign[x], second[x] = i.split()
            x += 1
        # each line
        for prob in problems:
            prob_split = prob.split()
            first = prob_split[0]
            second = prob_split[2]
            sign = prob_split[1]
            line = str(
                "--" + "-" * (len(str(max(int(first), int(second))))) + "")

            arranged = [f"{first:>{len(line) + 1 }}", '\n', sign,
                        f"{second:>{len(line) - 2 }}", '\n', line, '\n']
            #print(' '.join(arranged))

            arranged_problems += ' '.join(arranged) + '\n'

        return arranged_problems
