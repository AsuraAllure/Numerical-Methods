import math


def f(x): return 3 * math.cos(x) - math.exp(x)


epsilon = 0.5 * 10 ** -5

x1 = 0
x2 = math.pi / 2

count_iteration = 0

while abs(x2 - x1) > epsilon:
    mid = (x2 + x1) / 2

    if f(x2) == 0 or f(x1) == 0 or f(mid) == 0:
        break

    if f(mid) > 0:
        x1 = mid
    else:
        x2 = mid

    count_iteration += 1

print(count_iteration, x1, x2)
