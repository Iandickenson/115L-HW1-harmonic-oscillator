# Problem 1
import numpy as np


def recur(n):
    aold = 1
    anew = 1
    coeff = np.array([])
    m = 0
    if n % 2 != 0:
        m = 1
    while aold != 0:
        coeff = np.append(coeff, 0)
        coeff = np.append(coeff, aold)
        anew = aold * -2 * (n - m) /((m+2)*(m+1))
        # print(anew) this was to check it was working properly, not needed for now
        aold = anew
        m += 2
    if n % 2 == 0:
        coeff = coeff[1::]
    return coeff

print(recur(4))