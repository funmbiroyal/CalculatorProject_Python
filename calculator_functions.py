def add(num1, num2):
    return num1 + num2


def product(num1, num2):
    if type(num1) == str or type(num2) == str:
        raise TypeError(print("enter an integer"))
    return num1 * num2


def difference(num1, num2):
    return num1 - num2


def quotient(num1, num2):
    return num1 / num2
