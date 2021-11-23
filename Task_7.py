from random import randint


def gen():
    global a
    a = randint(0, 10)
    yield a


def fact(n):
    i = 1
    n1 = 0

    while i <= n:
        result = n * i + n1
        i = i + 1
        n1 = n * i
    return result


a = next(gen())


print(fact(a))
