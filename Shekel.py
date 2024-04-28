from Dollar import Dollar  # Importing the Dollar class for reference and initialization


# Shekel class representing the Shekel currency and associated operations
class Shekel(object):

    def __init__(self, val):
        # Constructor that initializes a Shekel object with a given value
        D = Dollar(val)  # Create a Dollar object to fetch currency rates
        self._val = val  # Set the initial value for the Shekel
        self.rates = D.rates  # Get the exchange rates from the Dollar class

    def __repr__(self):
        # Returns a string representation of the Shekel object
        return f'Shekel({self._val})'

    def __str__(self):
        # Returns a more user-friendly string representation of the Shekel object
        return f'Shekel nis {self._val}'

    def amount(self):
        # Returns the amount or value of the Shekel object
        return self._val

    def get_val(self):
        # Alias for `amount` method; returns the value of the Shekel object
        return self._val

    def __add__(self, other):
        # Defines the addition operator for Shekel
        # Returns the sum of the values of this Shekel object and another currency object
        return self.amount() + other.amount()

    def __sub__(self, other):
        # Defines the subtraction operator for Shekel
        # Returns the difference between the values of this Shekel object and another currency object
        return self.amount() - other.amount()
