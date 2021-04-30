class Calculator(object):

    @classmethod
    def add(cls, num1: int, num2: int) -> int:
        return num1 + num2

    @classmethod
    def product(cls, num1: int, num2: int) -> int:
        if type(num1) == str or type(num2) == str:
            raise TypeError
        return num1 * num2

    @classmethod
    def difference(cls, num1: int, num2: int) -> int:
        return num1 - num2

    @classmethod
    def quotient(cls, num1, num2: int) -> int:
        return num1 / num2
