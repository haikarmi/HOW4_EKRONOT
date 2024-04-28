from Dollar import Dollar


class Shekel(object):

    def __init__(self, val):
        D = Dollar(val)
        self._val = val
        self.rates = D.rates

    def __repr__(self):
        return (f'Shekel({self._val})')

    def __str__(self):
        return f'Shekel nis {self._val} '


    def amount(self):
        return self._val

    def get_val(self):
        return self._val

    def __add__(self, other):
        return self.amount() + other.amount()

    def __sub__(self, other):
        return self.amount() - other.amount()
