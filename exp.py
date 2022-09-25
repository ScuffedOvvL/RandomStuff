# Implementation of the square-and-multiply algorithm


# Convert decimal into binary
def binary(d):
    b = ""
    while d != 0:
        if d % 2 == 1:
            b += "1"
        else:
            b += "0"
            d //= 2
    return b[::-1]
	

# Convert binary into decimal
def decimal(b):
    d, e = 0, len(b)-1
    for _, v in enumerate(b):
        d += int(v) * 2 ** e
        e -= 1
    return d


def exp(x, y, n=None):
    r = x
    y = binary(y)

    for i in range(len(y)-1):
        r = (r * r) if n == None else (r * r) % n
        if y[i+1] == "1":
            r = (r * x) if n == None else (r * x) % n
    return r
