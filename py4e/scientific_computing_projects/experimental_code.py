def arithmetic_arranger(problems, solve=False):
    # TOO Many Problems Error
    if len(problems) > 5:
        return "Error: Too many problems."

    first = ''  # The First Operand
    second = ''  # The Operator and the Second Operand
    dash = ''  # The dashline
    solution = ''  # The Solution

    for problem in problems:
        problem = problem.split()  # String into List Conversion

        # Check for Unsupported Operand
        if problem[1] == '+' or problem[1] == '-':
            pass
        else:
            return "Error: Operator must be '+' or '-'."

        # Check for Operand Size
        if len(problem[0]) > 4 or len(problem[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Everything Else
        first += problem[0].rjust(len(max(problem)) + 2) + "\t"
        second += problem[1] + problem[2].rjust(len(max(problem)) + 1) + "\t"
        dash += '-' * (len(max(problem)) + 2) + "\t"

        # The Solutions and the Last Error Check
        try:

            if problem[1] == "+":
                add = int(problem[0]) + int(problem[2])
                solution += str(add).rjust(len(max(problem)) + 2) + "\t"

            else:
                sub = int(problem[0]) - int(problem[2])
                solution += str(sub).rjust(len(max(problem)) + 2) + "\t"

        except:
            return 'Error: Numbers must only contain digits.'

    if solve == True:
        return first + "\n" + second + "\n" + dash + "\n" + solution
    else:
        return first + "\n" + second + "\n" + dash + "\n"
