import math

# converts list l of strings to list of ints
def strListToInt(l):
    r = []
    for i in l:
        r.append(int(i))
    return r

# calculates x from quadratic ax^2 + bx + c = 0
def quadraticFormula(a, b, c):
    r = []
    for i in [1, -1]:
        try:
            num = -b + i * math.sqrt(math.pow(b, 2) - 4 * a * c)
        except ValueError:
            return []
        den = 2 * a
        r.append(num / den)
    return r

# lists all positave and negative factors of n
def factors(n):
    if n < 0: n *= -1
    if n == 0: return [0]
    r = []
    for i in range(1, n + 1):
        if n % i == 0:
            r.append(i)
    nr = []
    for i in r:
        nr.append(-i)
    for i in nr:
        r.append(i)
    return r

# removes duplicates from list l
def removeDuplicates(l):
    r = []
    for i in l:
        if i not in r:
            r.append(i)
    return r