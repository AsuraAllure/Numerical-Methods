import math

epsilon = 0.5 * 10 ** -5
count_iteration = 0


def f(x): return 3 * math.cos(x) - math.exp(x)


def df(x): return math.log(3) + math.log(math.cos(x))


x1 = math.pi / 8

while abs(f(x1) / df(x1)) > epsilon:
    x1 = df(x1)
    count_iteration += 1

print(count_iteration, x1)
