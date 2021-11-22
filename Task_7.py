def fact(n):
    i = 1
    n1 = 0
    while i <= n:
        result = n*i + n1
        i = i + 1
        n1 = n*i
    return result
        
def gen(yeild=None):
    from random import randint
    randint(0)
        yeild