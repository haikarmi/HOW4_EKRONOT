# Importing necessary classes to handle different currencies.
from Euro import Euro  # Euro class for handling Euro currency operations
from Dollar import Dollar  # Dollar class for handling Dollar currency operations
from Shekel import Shekel  # Shekel class for handling Shekel currency operations


def add(coin1, coin2):
    # Adds two currency objects, coin1 and coin2, and returns a new object
    # of the same type as coin1 with the calculated sum.
    temp = coin1 + coin2  # The sum of the two coins
    type_coin = type(coin1)  # Determine the type of coin1

    # Return a new instance of the corresponding currency class with the sum
    if type_coin == Dollar:
        s = Dollar(temp)
        s.set_val(temp)  # Set the value of the Dollar object
        return s
    elif type_coin == Euro:
        s = Euro(temp)
        s.set_val(temp)  # Set the value of the Euro object
        return s
    else:  # Default to Shekel if not Dollar or Euro
        s = Shekel(temp)
        return s


def sub(coin1, coin2):
    # Subtracts coin2 from coin1 and returns a new object of the same type as coin1.
    # Raises a ValueError if the result is negative.
    temp = coin1 - coin2  # The result of subtracting coin2 from coin1
    if temp < 0:
        raise ValueError("The amount is less than 0")  # Check for negative results

    type_coin = type(coin1)  # Determine the type of coin1

    # Return a new instance of the corresponding currency class with the difference
    if type_coin == Dollar:
        s = Dollar(temp)
        s.set_val(temp)  # Set the value of the Dollar object
        return s
    elif type_coin == Euro:
        s = Euro(temp)
        s.set_val(temp)  # Set the value of the Euro object
        return s
    else:  # Default to Shekel if not Dollar or Euro
        s = Shekel(temp)
        return s


def coerce_apply(operator_name, coin1, coin2):
    # Applies a specified operator (like 'add' or 'sub') to two currency objects,
    # converts the result to Shekel, and returns a new Shekel object with the calculated value.
    # Uses `eval` to dynamically evaluate the specified operator.
    return Shekel(eval(operator_name)(coin1, coin2).amount())  # Apply operator and convert to Shekel


def apply(operator_name, coin1, coin2):
    # Applies a specified operator to two currency objects and returns the result.
    # Converts between currencies using predefined rates.
    return eval(operator_name)(coin1, coin2)  # Apply operator to the two coins


if __name__ == '__main__':
    # This block contains examples of how the functions and classes are used.

    # Creating a Shekel object with an initial value of 50
    s = Shekel(50)

    # Initializing a rates dictionary with custom exchange rates

    # Creating Dollar and Euro objects with an initial value of 50
    d = Dollar(2000)
    e = Euro(50)
    print(d.amount())

    # Printing the amounts of Dollar and Euro objects
    print(d.amount())  # Dollar amount
    print(e.amount())  # Euro amount

    # Demonstrating addition between Dollar and Shekel
    print(d + s)  # Output the result of Dollar + Shekel

    # Using the add function to add Dollar and Euro
    print(add(d, e))  # Output the result of add function (Dollar + Euro)

    # Using the sub function to subtract Dollar from Euro
    # print(sub(e, d))  # Output the result of sub function (Euro - Dollar)

    # Using eval to recreate a Dollar object from its representation
    z = eval(repr(d))  # Recreate Dollar object from its representation
    print(z.amount())  # Print the amount of the recreated Dollar object

    # Using the apply function with 'add' to add Shekel and Dollar
    print(apply('add', s, d))  # Output the result of applying 'add' to Shekel and Dollar

    # Demonstrating operations between different currencies using apply and coerce_apply
    print(apply('add', Dollar(50), Euro(20)))  # Apply 'add' between Dollar and Euro
    print(apply('sub', Dollar(50), Euro(20)))  # Apply 'sub' between Dollar and Euro
    print(coerce_apply('add', Dollar(50), Euro(20)))  # Coerce-apply 'add' and convert to Shekel
    print(coerce_apply('sub', Dollar(50), Euro(20)))  # Coerce-apply 'sub' and convert to Shekel
