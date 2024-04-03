# from Euro import Euro
# from Dollar import Dollar

class Shekel(object):
    def __init__(self, val):
        self.rates = {("dollar", "nis"): 4, ("euro", "nis"): 8}
        self._val = val
        self.rates = {("dollar", "nis"): 4, ("euro", "nis"): 8,
                      ("dollar", "euro"): (self.rates["dollar", "nis"]) / (self.rates["euro", "nis"]),
                      ("euro", "dollar"): (self.rates["euro", "nis"]) / (self.rates["dollar", "nis"]),
                      ("nis", "dollar"): 1 / (self.rates["dollar", "nis"]),
                      ("nis", "euro"): 1 / (self.rates["euro", "nis"])}


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

