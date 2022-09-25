#Implementation of the Euclidean and Extended Euclidean algorithm


def gcd(a, b):
    r = a % b
    while r != 0:
        a, b = b, r
        r = a % b
    return b


def xgcd(a, b):
    s0, s1, t0, t1 = 1, 0, 0, 1
    q, r = divmod(a, b)
    while r != 0:
        s0, s1 = s1 - (q * s0), s0
        t0, t1 = t1 - (q * t0), t0
        a, b = b, r
        q, r = divmod(a, b)
		
    s0, t0 = t0, s0
    return b, s0, t0
		
		
def mod_inverse(a, b):
    g, s, t = xgcd(a, b)
    if g != 1:
        return None
    return s % b


def lcm(a, b):
    return a * b // gcd(a, b)
	

# Calculate legendre symbol using Euler's criterion
def legendre_symbol(a, p):
    if p % 2 == 0:
        return None
    if gcd(a, p) != 1:
        return 0
    if pow(a, p//2, p) == 1:
        return 1
    if pow(a, p//2, p) == p-1:
        return -1
    return pow(a, p//2, p)
