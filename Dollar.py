val_1 = float(input("Enter dollar to shekel conversion rates\n"))
val_2 = float(input("Enter euro to shekel conversion rates\n"))

class Dollar(object):
    def __init__(self, val):
        self.rates = {("dollar", "nis"): val_1, ("euro", "nis"): val_2}
        self._val = val
        self.rates = {("dollar", "nis"): val_1, ("euro", "nis"): val_2,
                      ("dollar", "euro"): (self.rates["dollar", "nis"]) / (self.rates["euro", "nis"]),
                      ("euro", "dollar"): (self.rates["euro", "nis"]) / (self.rates["dollar", "nis"]),
                      ("nis", "dollar"): 1 / (self.rates["dollar", "nis"]),
                      ("nis", "euro"): 1 / (self.rates["euro", "nis"])}

    def __repr__(self):
        return (f'Dollar({self._val})')

    def __str__(self):
        return f'dollar $ {self._val} '

    def amount(self):
        return self._val * self.rates["dollar", "nis"]

    def get_val(self):
        return self._val

    def __add__(self, other):
        return  self.amount() + other.amount()
    def __sub__(self, other):
        return self.amount() - other.amount()


    def set_val(self, val):
        self._val = val * self.rates["nis", "dollar"]
