def do_operation(self, other, operation):
    if (operation == '+'):
        if isinstance(other, self.__class__):
            return self.__class__(self.name, self.amount + other.amount)
        elif (isinstance(other, int) or isinstance(other, float)):
            return self.__class__(self.name, self.amount + other)
        else:
            return self.__class__(self.name, self.amount + other.amount * other.exchange_rate / self.exchange_rate)
    elif (operation == '-'):
        if isinstance(other, self.__class__):
            return self.__class__(self.name, self.amount - other.amount)
        elif (isinstance(other, int) or isinstance(other, float)):
            return self.__class__(self.name, self.amount - other)
        else:
            return self.__class__(self.name, self.amount - other.amount * other.exchange_rate / self.exchange_rate)
    elif (operation == '*'):
        if isinstance(other, self.__class__):
            return self.__class__(self.name, self.amount * other.amount)
        elif (isinstance(other, int) or isinstance(other, float)):
            return self.__class__(self.name, self.amount * other)
        else:
            return self.__class__(self.name, self.amount * other.amount * other.exchange_rate / self.exchange_rate)
    elif (operation == '/'):
        if isinstance(other, self.__class__):
            return self.__class__(self.name, self.amount / other.amount)
        elif (isinstance(other, int) or isinstance(other, float)):
            return self.__class__(self.name, self.amount / other)
        else:
            return self.__class__(self.name, self.amount / other.amount * other.exchange_rate / self.exchange_rate)
    elif (operation == '+='):
        if isinstance(other, self.__class__):
            self.amount += other.amount
        elif (isinstance(other, int) or isinstance(other, float)):
            self.amount += other
        else:
            self.amount += other.amount * other.exchange_rate / self.exchange_rate
        return self
    elif (operation == '-='):
        if isinstance(other, self.__class__):
            self.amount -= other.amount
        elif (isinstance(other, int) or isinstance(other, float)):
            self.amount -= other
        else:
            self.amount -= other.amount * other.exchange_rate / self.exchange_rate
        return self
    elif (operation == '*='):
        if isinstance(other, self.__class__):
            self.amount *= other.amount
        elif (isinstance(other, int) or isinstance(other, float)):
            self.amount *= other
        else:
            self.amount *= other.amount * other.exchange_rate / self.exchange_rate
        return self
    elif (operation == '/='):
        if isinstance(other, self.__class__):
            self.amount /= other.amount
        elif (isinstance(other, int) or isinstance(other, float)):
            self.amount /= other
        else:
            self.amount /= other.amount * other.exchange_rate / self.exchange_rate
        return self


class BaseWallet:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __add__(self, other):
        return do_operation(self, other, '+')

    def __radd__(self, other):
        return self.__class__(self.name, other + self.amount)

    def __iadd__(self, other):
        return do_operation(self, other, '+=')

    def __sub__(self, other):
        return do_operation(self, other, '-')

    def __rsub__(self, other):
        return self.__class__(self.name, other - self.amount)

    def __isub__(self, other):
        return do_operation(self, other, '-=')

    def __mul__(self, other):
        return do_operation(self, other, '*')

    def __rmul__(self, other):
        return self.__class__(self.name, other * self.amount)

    def __imul__(self, other):
        return do_operation(self, other, '*=')

    def __truediv__(self, other):
        return do_operation(self, other, '/')

    def __rtruediv__(self, other):
        return self.__class__(self.name, other / self.amount)

    def __itruediv__(self, other):
        return do_operation(self, other, '/=')

    def __eq__(self, other):
        return ((self.__class__ is other.__class__) and (self.amount == other.amount))

    def __str__(self):
        name = self.__class__.__name__.replace('Wallet', ' Wallet')
        return name + f' {self.name} {self.amount}'

    def spend_all(self):
        if (self.amount > 0):
            self.amount = 0

    def to_base(self):
        return self.amount * self.exchange_rate


class RubbleWallet(BaseWallet):
    exchange_rate = 1

    def __init__(self, name, amount):
        super().__init__(name, amount)


class DollarWallet(BaseWallet):
    exchange_rate = 60

    def __init__(self, name, amount):
        super().__init__(name, amount)


class EuroWallet(BaseWallet):
    exchange_rate = 70

    def __init__(self, name, amount):
        super().__init__(name, amount)
