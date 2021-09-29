def fact(n):
    """
    Factorial function

    :arg n: Number
    :returns: factorial of n

    """
    if n == 0:
        return 1
    return n * fact(n -1)

if __name__=='__main__':
    n=int(input('Enter n value'))
    res = fact(n)
    print(res)