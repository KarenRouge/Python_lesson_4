from sys import argv
number = argv
from itertools import cycle
a = 0
for el in cycle([25, True, "Hello"]):
    if a > 15:
        break
    print(el)
    a += 1
