import numpy as np
def multiply(arr1, arr2): #multiplying an array by the derivative of g(z) = exp(-z^2 + 2z), g'(z)/g(z) = [-2, 2]. 
    #arr2 must be of length 2 for this function to work
    length = len(arr1) #length of leading polynomial 
    length2 = len(arr2) #length of lower order polynomial
    product = np.array([arr1[0] * arr2[0]]) # leading coefficient
    #print(product)
    for i in range(length-1):
        newcoeff = (arr1[i] * arr2[1]) + (arr1[i+1] * arr2[0]) #determining coefficient for term of order n by 
        # multiplying terms (n-1) and 1 and terms n and 0
        # print(newcoeff)
        product = np.append(product, newcoeff)
    product = np.append(product, arr1[length-1] * arr2[length2-1]) #last coefficient
    return product
a = np.array([4,0,4])
b = np.array([-2,2])
print(multiply(a,b))
print(multiply(multiply(a,b), b)) 
#this function should give the coefficients of the product of a polynomial with the derivative g'(z)/g(z)
#when applied n times, it should give the nth derivative of g(z), divided by g(z)