import math


hypotenuse = lambda x, y=1: round(math.sqrt(x ** 2 + y ** 2), 2)

values_x = [9, 8, 7, 6]
output1 = list(map(hypotenuse, values_x))
print(f'Коли передається один список: {output1}')

values_y = [1, 2, 3, 4]
output2 = list(map(hypotenuse, values_x, values_y))
print(f'Коли передається два списки: {output2}')
