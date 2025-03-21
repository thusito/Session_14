import china

china.cook()
china.greet()

import Austrian

Austrian.cook()
Austrian.greet()

try:
    import romania
except ModuleNotFoundError:
    print("i don't know romania")

import sys
china.cook()
china.greet()

def cook():
    print("We are making paella")
cook()

def is_prime(n):
    if n<=1:
        return False
    for i in range(1,n):
        if n%i==0:
            return False
    return True
print("prime numbers")
print(is_prime(5))
print(is_prime(25))
print(is_prime(201))
print(is_prime(19))

from LATAM.argentina import cook as argentina_cook
from LATAM.Peru import cook as peru_cook
from LATAM.Mexico.yucatan import cook as yucatan_cook

yucatan_cook()
argentina_cook()