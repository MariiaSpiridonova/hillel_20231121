import random
from tabulate import tabulate

n = int(input("Введіть ціле число більше 5 >>> "))
m = int(input("Введіть ціле число більше 5 >>> "))

matrix = [[random.randint(1, 100) for i in range(m)] for j in range(n)]

# for line in matrix:
#     print(*line)

print(tabulate(matrix))

for j in range(n):
    matrix[j][m-1], matrix[j][m-2] = matrix[j][m-2], matrix[j][m-1]

print(tabulate(matrix))
