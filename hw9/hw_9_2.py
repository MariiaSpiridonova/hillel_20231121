import random

dictionary = {i: random.randint(2, 12) for i in range(1, 21)}
print(dictionary)

values_product = 1
for value in dictionary:
    values_product *= dictionary[value]

print(f'{values_product:,}')
