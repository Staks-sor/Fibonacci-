import numpy


def fiba(n):
    return (numpy.matrix([[2, 1], [1, 1]]) ** (n // 2))[0, (n + 1) % 2]


fib = [fiba(i) for i in range(10)]
lab = [i for i in fib if i % 2 == 0]
print(lab)