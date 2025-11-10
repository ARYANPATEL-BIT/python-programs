import math

def sin(num):
    return math.sin(math.radians(num))

def sqrt(num):
    sqrt = num**0.5
    return sqrt

def factorial(num):
    total = 1
    for i in range(1,num+1):
        total *= i
    return total

def power(num,pow):
    powered = num ** pow
    return powered

