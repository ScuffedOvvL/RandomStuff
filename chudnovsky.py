# Implementation of the Chudnovsky algorithm to calculate decimal digits of pi


from decimal import Decimal, getcontext
from math import factorial, sqrt


def chudnovsky(n):
    getcontext().prec = n+3
    s = 0
	
    for k in range(n // 14 + 1):
        num = (factorial(6*k)) * (545140134*k+13591409)
        don = (factorial(3*k)) * (factorial(k)**3) * (-262537412640768000)**k
        s += Decimal(num) / Decimal(don)
		
    t = 426880 * Decimal(10005).sqrt()
    pi = Decimal(t) / Decimal(s)
    return str(pi)[:-2]
