import math


def f(x): return 3 * math.cos(x) - math.exp(x)


def df(x): return (-3) * math.sin(x) - math.exp(x)



def newPoint(x1, x0):
    return x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))


x0 = math.pi / 2
x1 = 0
x2 = newPoint(x1, x0)

epsilon = 0.5 * 10 ** -5
count_iteration = 1

while abs(f(x2) / df(x2)) > epsilon:
    x1, x2 = x2, newPoint(x2, x1)
    count_iteration += 1

print(count_iteration, x1, x2)
