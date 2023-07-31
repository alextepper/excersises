# Exercise 1: Currencies

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        if self.amount > 1:
            return f"{self.amount} {self.currency}s"
        else:
            return f"{self.amount} {self.currency}"
    def __int__(self):
        return self.amount

    def __repr__(self):
        return f"{self.amount} {self.currency}"

    def __add__(self, other):
        if type(other) == int:
            return self.amount + other
        elif type(other) == Currency:
            if self.currency == other.currency:
                return Currency(self.currency, self.amount + other.amount)
            else:
                raise Exception(f"Cannot add between Currency type {self.currency} and {other.currency}")
        else:
            raise Exception(f"Cannot add between {type(self)} and {type(other)}")

    def __iadd__(self, other):
        if type(other) == int:
            return Currency(currency=self.currency, amount=self.amount + other)
        elif type(other) == Currency:
            if self.currency == other.currency:
                return Currency(currency=self.currency, amount=self.amount + other.amount)
            else:
                raise Exception(f"Cannot add between Currency type {self.currency} and {other.currency}")
        else:
            raise Exception(f"Cannot add between {type(self)} and {type(other)}")

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(c1)

c1 += c2

print(c1)

print(c1 + c3)