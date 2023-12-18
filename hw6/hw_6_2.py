import random
from tabulate import tabulate

n = int(input("Введіть ціле число більше 5 >>> "))
m = int(input("Введіть ціле число більше 5 >>> "))

matrix = [[random.randint(1, 100) for i in range(n)] for j in range(m)]

# for line in matrix:
#     print(*line)

print(tabulate(matrix))

matrix[m-1], matrix[m-2] = matrix[m-2], matrix[m-1]

print(tabulate(matrix))
