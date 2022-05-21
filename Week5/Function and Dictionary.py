# Given a number n, define a function named printDict() which can print a dictionary where the keys are numbers
# between 1 and n (both included) and the values are square of keys. The function printDict() doesn't take any
# argument.

n = int(input())


def printDict():
    d = dict()
    for i in range(1, n + 1):
        d[i] = i * i

    print(d)


printDict()
