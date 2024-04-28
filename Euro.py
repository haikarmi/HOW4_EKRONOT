from Dollar import Dollar  # Importing the Dollar class to fetch exchange rates

# Euro class representing the Euro currency and associated operations
class Euro(object):
    def __init__(self, val):
        # Constructor that initializes a Euro object with a given value
        D = Dollar(val)  # Create a Dollar object to fetch currency rates
        self._val = val  # Set the initial Euro value
        self.rates = D.rates  # Get the exchange rates from the Dollar object

    def __repr__(self):
        # Returns a formal representation of the Euro object
        return f'Euro({self._val})'

    def __str__(self):
        # Returns a more user-friendly string representation of the Euro object
        return f'Euro € {self._val}'

    def amount(self):
        # Returns the Euro value converted to Shekel using the appropriate conversion rate
        return self._val * self.rates[("euro", "nis")]

    def get_val(self):
        # Returns the raw Euro value without conversion
        return self._val

    def __add__(self, other):
        # Defines the addition operator for Euro
        # Returns the sum of this Euro's amount and another currency's amount converted to Shekel
        return self.amount() + other.amount()

    def __sub__(self, other):
        # Defines the subtraction operator for Euro
        # Returns the difference between this Euro's amount and another currency's amount converted to Shekel
        return self.amount() - other.amount()

    def set_val(self, val):
        # Sets the raw Euro value after converting it from Shekel
        self._val = val * self.rates[("nis", "euro")]  # Convert Shekel to Euro
