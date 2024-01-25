# Problem 3
import numpy as np
def hermite(u, n): 
    H_less1 = 1
    H_current = 1 * u
    for i in (2,n+1):
        H_new = (2*u*H_current) - (2*(i-1)*H_less1)
        H_less1 = H_current
        H_current = H_new
    return H_new

print(hermite(1,3))