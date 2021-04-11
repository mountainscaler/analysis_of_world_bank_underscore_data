def nth_power(n, power=2):
    '''
    Calculates power for number upto n.
    args:
        power: power for numbers to raise, default power is 2.
    '''
    return[i**power for i in range(n)]

print(nth_power(10))
