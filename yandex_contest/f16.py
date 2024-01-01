class Calculator:
    last = None

    def __init__(self):
        self.__history = list()

    def sum(self, a, b):
        result = a + b
        Calculator.last = f"sum({a}, {b}) == {round(result, 1)}"
        self.__history.append(Calculator.last)
        return result

    def sub(self, a, b):
        result = a - b
        Calculator.last = f"sub({a}, {b}) == {round(result, 1)}"
        self.__history.append(Calculator.last)
        return result

    def mul(self, a, b):
        result = a * b
        Calculator.last = f"mul({a}, {b}) == {round(result, 1)}"
        self.__history.append(Calculator.last)
        return result

    def div(self, a, b, mod=False):
        result = (a / b) if not mod else (a % b)
        Calculator.last = f"div({a}, {b}) == {round(result, 1)}"
        self.__history.append(Calculator.last)
        return result

    def history(self, n):
        if n <= len(self.__history):
            return self.__history[-n]

    @classmethod
    def clear(cls):
        cls.last = None