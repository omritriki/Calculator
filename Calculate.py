import re
from time import time


def Division(input):
    elements = re.split('÷', input)

    for j in range(len(elements)):
        if 'x' in elements[j]:
            elements[j] = Product(elements[j])

    if elements[1] == '0':
        # print("You can't divide by zero you dumbass")
        return "Error"

    return float(elements[0]) / float(elements[1])


def Product(input):
    product = 1

    elements = re.split('x', input)
    for j in range(len(elements)):
        if '÷' in elements[j]:
            elements[j] = Division(elements[j])
            if elements[j] == "Error":
                return "Error"

    for i in elements:
        product *= float(i)

    return product


def Calculate(input):
    equation = input.replace('=', '')
    answer = 0

    if input == '':
        return "Error"

    # Finding brackets
    if '(' in equation:
        brackets = equation.split('(', 1)[1].split(')')[0]
        solution = Calculate(brackets)
        if solution == "Error":
            return "Error"
        equation = equation.replace(brackets, str(solution))

    if equation[0].isdigit() == "Error":
        equation = '0' + equation

    if '-' in equation:
        equation = equation.replace('-', '+-')

    parts = re.split('\+', equation)

    if parts[0] == '0':
        parts[0] = int(0)

    for i in range(len(parts)):
        if parts[i] == None:
            return "Error"
        parts[i] = (parts[i].replace('(', '')).replace(')', '')
        if type(parts[i]) != type(int()):
            parts[i] = Product(parts[i])
            if parts[i] == "Error":
                return "Error"

    for j in parts:
        answer += float(j)

    if answer % 1 == 0:
        return int(answer)
    return answer


def Check(input):
    brackets = 0
    signs = "+-x÷"
    check = str(input)

    # special_chars = "+-x/()"
    # chars_only = re.sub(r'[0-9]', '', check)

    """
    for i in chars_only:
        if i not in special_chars:
            return "Error1"
    """
    print(check)
    while brackets >= 0:
        for j in range(len(check)):
            if check[j] == '(':
                brackets += 1
                if j != 0:
                    if check[j - 1] not in signs and check[j - 1] != '(':
                        return "Error2"
            if check[j] == ')':
                brackets -= 1
                print("j is ", j)
                print(len(check))
                if j != (len(check) - 1):
                    if check[j + 1] not in signs and check[j + 1] != ')':
                        return "Error3"
            if check[j] in signs:
                if check[j + 1] in signs:
                    return "Error4"

        break

    if brackets == 0:
        return str(Calculate(input))


"""
def main():
    print("Enter an equation:")
    equation = input()
    t0 = time()
    output = Check(equation)

    if output != False:
        print(f"Answer is {output}")
        t1 = time()
        print(f"Runtime is {float(t1 - t0)} seconds")
        return

    print("You entered an invalid equation")


if __name__ == '__main__':
    main()
"""
