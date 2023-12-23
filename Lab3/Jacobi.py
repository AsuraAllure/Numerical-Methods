A = [
    [1.73, 0.03, 0.2],
    [-0.1, 0.77, 0.46],
    [-0.07, -0.43, -0.59]
]

C = [2.39, 2.82, -2.7]

normaB = 0.845

x_k = [0, 0, 0]
x_k1 = [2.39, 2.82, -2.7]
n = 1
epsilon = 0.00005


def norma_vector(v1, v2):
    ma = abs(v1[0] - v2[0])
    for i in range(1, 3):
        if abs(v1[0] - v2[0]) > ma:
            ma = abs(v1[0] - v2[0])
    return ma


while norma_vector(x_k1, x_k) > (1 - normaB) / normaB * epsilon:
    for i in range(3):
        x_k[i] = x_k1[i]
        x_k1[i] = C[i] / A[i][i]
        for j in range(3):
            if j != i:
                x_k1[i] += -A[i][j] / A[i][i] * x_k[j]
    n += 1

print(x_k1)
print(n)
