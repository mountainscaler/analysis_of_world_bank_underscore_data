def nth_power(n, fn = lambda x: x**2):
    '''
    Calculates power for number upto n.
    '''
    return[fn(i) for i in range(n)]

print(nth_power(10))
