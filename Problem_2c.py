import numpy as np
def generating(u, n):
    # Use the generating function to return an array of the coefficients of the hermite polynomial and print it for 
    # n = 0 to n = 5
    hcoeff = np.array([1, 0, -2])
    polynomial = 0
    length = len(hcoeff)
    for i in range(length):
        polynomial = polynomial + (hcoeff[i] * u**i) #pluggin in u value into the polynomial to get value
    return polynomial
# print(generating(1,1))