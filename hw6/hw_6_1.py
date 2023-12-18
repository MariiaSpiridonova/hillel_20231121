import random

num = int(input("Введіть ціле число більше 0 >>> "))

matrix = [[random.randint(10, 99) for j in range(num)] for i in range(num)]

for line in matrix:
    print(*line)

sum_left_right = 0
sum_right_left = 0
for i in range(num):
    sum_left_right += matrix[i][i]
    sum_right_left += matrix[i][num-i-1]

print(f"Сума діагоналі зліва направо дорівнює {sum_left_right}")
print(f"Сума діагоналі зправа наліво дорівнює {sum_right_left}")

if num % 2 != 0 and num != 1:
    middle_num = num // 2
    print(f"Центральне число: {matrix[middle_num][middle_num]}")
elif num == 1:
    print(f"Центральне і єдине число в матриці: {matrix[0][0]}")
else:
    print("Парна кільсіть елементів матриці, немає центрального числа")
