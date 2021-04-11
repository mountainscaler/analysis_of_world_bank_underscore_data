def nth_power(n, fn = lambda x: x**3):
    '''
    Calculates power for number upto n.
    args:
        power: power for numbers to raise, default power is 3.
    '''
    return[fn(i) for i in range(n)]

print(nth_power(10))
