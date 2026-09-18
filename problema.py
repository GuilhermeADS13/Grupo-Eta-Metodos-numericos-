import math

#Problema inicial
#Equação dada no projeto: E - R * i - g(i) = 0
#Sendo e = 10, r = 2, g(i) = i**3

def f(i):
    return 10 - 2 * i - (i ** 3)



def f_linha(i):
    return -2 - 3 * (i ** 2)


eps1 = 1e-4
eps2 = 1e-4
kmax = 50
