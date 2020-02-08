def half(x):
    return x / 2

def double(x):
    return x * 2

def facts(x):
    numberOfFactors = 1
    for i in range(1, int(x /2) + 1):
        if x % i == 0:
            numberOfFactors += 1
    return numberOfFactors

def power(a, b):
    return a ** b