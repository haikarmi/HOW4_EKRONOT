# Read conversion rates from user input
val_1 = float(input("Enter dollar to shekel conversion rate\n"))  # Conversion rate from Dollar to Shekel
val_2 = float(input("Enter euro to shekel conversion rate\n"))  # Conversion rate from Euro to Shekel

# Dollar class representing the Dollar currency and associated operations
class Dollar(object):
    def __init__(self, val):
        # Constructor that initializes a Dollar object with a given value
        self._val = val  # Set the initial Dollar value
        # Initialize exchange rates for different currency conversions
        self.rates = {
            ("dollar", "nis"): val_1,  # Dollar to Shekel rate
            ("euro", "nis"): val_2,  # Euro to Shekel rate
            ("dollar", "euro"): val_1 / val_2,  # Dollar to Euro rate
            ("euro", "dollar"): val_2 / val_1,  # Euro to Dollar rate
            ("nis", "dollar"): 1 / val_1,  # Shekel to Dollar rate
            ("nis", "euro"): 1 / val_2,  # Shekel to Euro rate
        }

    def __repr__(self):
        # Returns a formal representation of the Dollar object
        return f'Dollar({self._val})'

    def __str__(self):
        # Returns a user-friendly string representation of the Dollar object
        return f'dollar $ {self._val}'

    def amount(self):
        # Returns the Dollar amount converted to Shekel using the conversion rate
        return self._val * self.rates[("dollar", "nis")]

    def get_val(self):
        # Returns the raw Dollar value without conversion
        return self._val

    def __add__(self, other):
        # Defines the addition operator for Dollar
        # Returns the sum of this Dollar amount and another currency's amount converted to Shekel
        return self.amount() + other.amount()

    def __sub__(self, other):
        # Defines the subtraction operator for Dollar
        # Returns the difference between this Dollar amount and another currency's amount converted to Shekel
        return self.amount() - other.amount()

    def set_val(self, val):
        # Sets the raw Dollar value after converting it from Shekel
        self._val = val * self.rates[("nis", "dollar")]  # Convert Shekel to Dollar
