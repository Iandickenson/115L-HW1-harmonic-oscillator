# Problem 2
# was gonna try and use sympy to print out the hermite polynomial in terms of u then plug in the value
import numpy as np


def derivative(arr): # derivative of a polynomial
    length = len(arr) - 1
    deriv = np.array([])
    for i in range(length):
        print(i)
        print(length - i)
        deriv = np.append(deriv, (length - i)*arr[i])
    return deriv

print(derivative([6, 1, 2, 0]))
