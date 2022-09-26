# Implementation of some factorization algorithms
from math import gcd, sqrt, isqrt, ceil


def pollard_rho(n):
    x, y, d = 2, 2, 1
    while True:
        x = (x * x + 1) % n
        y = (y * y + 1) % n
        y = (y * y + 1) % n
        d = gcd(x - y, n)
        if d > 1:
            return n//d, d
    return


def fermat_factorize(n):
    x = isqrt(n) +1	
    while True:
        y = isqrt(x*x-n)
        p, q = x-y, x+y
        if p*q == n:
            return p, q
        x += 1
    return


def trial_division(n):
    p = ceil(sqrt(n))
    
    while True:
        if n % p == 0:
            return n//p, p
        p += 1
    return


def decompose(c):
    pf = []
    i = 2

    while c > 1:
        for _ in range(2, ceil(sqrt(c))+1):
            if c % i == 0:
                pf.append(i)
                c //= i
            else:
                i += 1
    return pf
