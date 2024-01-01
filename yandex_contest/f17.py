class BaseWallet:
    exchange_rate = 1
    
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __add__(self, other):
        money = ((self.to_base() + other.to_base()) / self.exchange_rate
                 if isinstance(other, BaseWallet) else self.amount + other)
        return self.__class__(self.name, money)

    def __radd__(self, other):
        return self.__class__(self.name, other + self.amount)

    def __iadd__(self, other):
        self.amount += (other.to_base() / self.exchange_rate) if isinstance(other, BaseWallet) else other
        return self

    def __sub__(self, other):
        money = ((self.to_base() - other.to_base()) / self.exchange_rate
                 if isinstance(other, BaseWallet) else self.amount - other)
        return self.__class__(self.name, money)

    def __rsub__(self, other):
        return self.__class__(self.name, other - self.amount)

    def __isub__(self, other):
        self.amount -= (other.to_base() / self.exchange_rate) if isinstance(other, BaseWallet) else other
        return self
    
    def __mul__(self, other):
        money = ((self.to_base() * other.to_base()) / self.exchange_rate
                 if isinstance(other, BaseWallet) else self.amount * other)
        return self.__class__(self.name, money)

    def __rmul__(self, other):
        return self.__class__(self.name, other * self.amount)

    def __imul__(self, other):
        self.amount *= (other.to_base() / self.exchange_rate) if isinstance(other, BaseWallet) else other
        return self
    
    def __truediv__(self, other):
        money = ((self.to_base() / other.to_base()) / self.exchange_rate
                 if isinstance(other, BaseWallet) else self.amount / other)
        return self.__class__(self.name, money)

    def __rtruediv__(self, other):
        return self.__class__(self.name, other / self.amount)

    def __itruediv__(self, other):
        self.amount /= (other.to_base() / self.exchange_rate) if isinstance(other, BaseWallet) else other
        return self
    
    def __eq__(self, other):
        return ((self.__class__ is other.__class__) and (self.amount == other.amount))

    def spend_all(self):
        self.amount = 0 if self.amount > 0 else self.amount

    def to_base(self):
        return self.amount * self.exchange_rate


class RubbleWallet(BaseWallet):
    def __str__(self):
        return f"Rubble Wallet {self.name} {self.amount}"


class DollarWallet(BaseWallet):
    exchange_rate = 60

    def __str__(self):
        return f"Dollar Wallet {self.name} {self.amount}"


class EuroWallet(BaseWallet):
    exchange_rate = 70

    def __str__(self):
        return f"Euro Wallet {self.name} {self.amount}"