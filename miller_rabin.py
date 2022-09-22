"""
Implementation of the Miller-Selfridge-Rabin primality test
Standard error probability is 2 ^ -100 (50 rounds)
Trial division test with primes below 2000
Deterministic version up to a value of 3,317,044,064,679,887,385,961,980

NOTE: This library should NEVER be used for any cryptographic purposes!
"""
from random import randint


LIMIT = 3317044064679887385961980

PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987, 1993, 1997, 1999)

STAR_WITNESSES = PRIMES[:13]


# Simple divisibility test
def divisible(a, b):
    return not a % b


# Function that generates random odd numbers
def rand_odd(bits):
	while (num := randint(2**(bits-1), (2**bits)-1)) and divisible(num, 2):
		continue
	return num


# Function that generates random even numbers
def rand_even(bits):
	while (num := randint(2**(bits-1), (2**bits)-1)) and not divisible(num, 2):
		continue
	return num


# Fermat prp test to rule out most of the composite numbers
def fermat_prp(b, n):
    if pow(b, n-1, n) == 1:
        return True
    return False


def trial_division(n):
    if n in PRIMES:
        return True
    
    if n < 2:
        return False
    
    for prime in PRIMES:
        if divisible(n, prime):
            return False
    return True


def sprp(b, n):
    u, d = 0, n-1
    while divisible(d, 2):
        u += 1
        d //= 2
    
    z = pow(b, d, n)
    
    if z != 1 and z != n-1:
        j = 1
        while j <= u-1 and z != n-1:
            z = pow(z, 2, n)
            if z == 1:
                return False
            j += 1
        if z != n-1:
            return False
    return True


# Sprp-test with random bases
def miller_rabin(n, rounds=50):
    if n == 2 or n == 3:
        return True

    if not trial_division(n):
        return False

    if not fermat_prp(2, n):
        return False

    for _ in range(rounds):
        a = randint(2, n-2)
        if not sprp(a, n):
            return False
    return True
    

# Deterministic version up to a specific limit
def mr_deterministic(n):
    if n == 2 or n == 3:
        return True

    if not trial_division(n):
        return False
        
    if n < 2047:
        if not sprp(2, n):
            return False
        return True
            
    if n <= LIMIT:
        for wts in STAR_WITNESSES:
            if not sprp(wts, n):
                return False
        return True
    return
    

# Prime sieve that uses the deterministic version
def mrdt_sieve(n):
    if n > LIMIT:
        return None
    primes = []
    for x in range(2, n):
        if mr_deterministic(x):
            primes.append(x)
    return primes


# Uses miller_rabin function to generate probable primes
def generate_probable(bits, rounds=50):
    while (probable := rand_odd(bits)) and not miller_rabin(probable, rounds):
        continue
    return probable


# Uses deterministic version to generate proven primes
def generate_proven(bits):
    while (proven := rand_odd(bits)) and not mr_deterministic(proven) and not proven.bit_length() > 82:
        continue
    return proven if proven < LIMIT else None


