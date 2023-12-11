class Calculator:
    last = None

    def __init__(self):
        self._list_history = list()

    def sum(self, a, b):
        Calculator.last = f'sum({a}, {b}) == ' + str(round(a + b, 1))
        self._list_history.append(Calculator.last)
        return a + b

    def sub(self, a, b):
        Calculator.last = f'sub({a}, {b}) == ' + str(round(a - b, 1))
        self._list_history.append(Calculator.last)
        return a - b

    def mul(self, a, b):
        Calculator.last = f'mul({a}, {b}) == ' + str(round(a * b, 1))
        self._list_history.append(Calculator.last)
        return a * b

    def div(self, a, b, mod=False):
        res = (a % b) if mod else (a / b)
        Calculator.last = f'div({a}, {b}) == ' + str(round(res, 1))
        self._list_history.append(Calculator.last)
        return res

    def history(self, n):
        if n <= len(self._list_history):
            return self._list_history[-n]

    @classmethod
    def clear(cls):
        cls.last = None
