def factorial(x):
    if x == 1:
        return 1
    else:
        x = factorial(x-1) * x
    return x
