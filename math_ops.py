# Logika Scientific

import math

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error"
    return a / b

def pangkat(a, b):
    return math.pow(a, b)

def akar(a):
    return math.sqrt(a)

def sin(a):
    return math.sin(math.radians(a))

def cos(a):
    return math.cos(math.radians(a))

def tan(a):
    return math.tan(math.radians(a))

def log(a):
    return math.log10(a)

def ln(a):
    return math.log(a)

def pi():
    return math.pi
