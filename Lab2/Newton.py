import math

x = math.pi/2

def f(x): return 3 * math.cos(x) - math.exp(x)

def df(x): return (-3)*math.sin(x) - math.exp(x)


epsilon = 0.5 * 10 ** -5
count_iteration = 0

while abs(f(x) / df(x)) > epsilon:
    x = x - f(x) / df(x)
    count_iteration += 1

print(count_iteration, x)
