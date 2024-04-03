from Dollar import Dollar
from Shekel import Shekel


class Euro(object):
    def __init__(self, val):
        self.rates = {("dollar", "nis"): 3.72, ("euro", "nis"): 8}
        self._val = val
        self.rates = {("dollar", "nis"): 4, ("euro", "nis"): 8,
                      ("dollar", "euro"): (self.rates["dollar", "nis"]) / (self.rates["euro", "nis"]),
                      ("euro", "dollar"): (self.rates["euro", "nis"]) / (self.rates["dollar", "nis"]),
                      ("nis", "dollar"): 1 / (self.rates["dollar", "nis"]),
                      ("nis", "euro"): 1 / (self.rates["euro", "nis"])}

    def __repr__(self):
        return (f'Euro({self._val})')

    def __str__(self):
        return f'Euro € {self._val}'

    def amount(self):
        return self._val * self.rates["euro", "nis"]

    def get_val(self):
        return self._val

    def __add__(self, other):
        return self.amount() + other.amount()
    def __sub__(self, other):
        return self.amount() - other.amount()


    def set_val(self, val):
        self._val = val * self.rates["nis", "euro"]




