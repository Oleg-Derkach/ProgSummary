import doctest

def fact(n):
    '''
    >>> fact(1)
    1
    >>> fact(2)
    2
    >>> fact(3)
    14
    '''
    for i in range(1,n+1):
        i*=n
    return n


print(doctest.testmod())