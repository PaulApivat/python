import operator


def check_num(s):
    try:
        int(s)
        return True
    except:
        return False


def is_correct_format(problems):
    if len(problems) > 5:
        print('Error: Too many problems.')
    else:
        for item in problems:
            problem = item.split(' ')
            if not(check_num(problem[0]) and check_num(problem[2])):
                print('Error: Numbers must only contain digits.')
                correct_format = False
                break

            elif problem[1] is not '+' and problem[1] is not '-':
                print('Error: Operator must be ''+'' or ''-''.')
                correct_format = False
                break

            elif max(len(problem[0]), len(problem[2])) > 4:
                print('Error: Numbers cannot be more than four digits.')
                correct_format = False
                break

            else:
                correct_format = True
        return correct_format


def arithmetic_arranger(problems, solve=False):
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
        # first line
        for i in range(len(problems)):
            arranged_problems += str(" " * (len(str(max(int(first[i]), int(second[i])))) - len(
                str(first[i])) + 2) + first[i] + " "*4)

        arranged_problems += str("\n")
        # second line
        for i in range(len(problems)):
            arranged_problems += str(
                sign[i] + " " * (len(str(max(int(first[i]), int(second[i])))) - len(second[i]) + 1) + second[
                    i] + " "*4)
        arranged_problems += str("\n")
        # Third line
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


# For testing locally the output
print(arithmetic_arranger(["32 + 6986", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(
    ["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))
print(arithmetic_arranger(["44 + 815", "909 - 2",
                           "45 + 43", "123 + 49", "888 + 40", "653 + 87"]))
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(
    ["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True))
