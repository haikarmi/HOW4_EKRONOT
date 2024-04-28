from Dollar import Dollar


class Euro(object):
    def __init__(self, val):
            D = Dollar(val)
            self._val = val
            self.rates = D.rates

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




