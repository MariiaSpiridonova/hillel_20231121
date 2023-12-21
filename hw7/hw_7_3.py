n = int(input('Input number from 3 to 9 >>> '))

if n < 3 or n > 9:
    print("Invalid number of rows. Please enter a number between 3 and 9. Exit")
else:
    for i in range(1, n + 1):
        left_side = ''.join(str(j) for j in range(1, i + 1))
        right_side = left_side[-2::-1]
        row = left_side + right_side
        print(row.rjust(n * 2 - 1, ' '))
        # print(row.center(n * 2 - 1, ' '))
        # print(row.ljust(n * 2 - 1, ' '))
