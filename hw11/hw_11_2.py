import random

n = random.randint(1, 50)
z = random.randint(200, 400)


def prime_numbers_generator(n, z):
    for i in range(n, z + 1):
        is_prime = True
        for number in range(2, int(i ** 0.5) + 1):
            if i % number == 0:
                is_prime = False
                break
        if is_prime:
            yield i


print(f'Прості числа в діапазоні від {n} до {z}:')
for n in prime_numbers_generator(n, z):
    print(n, end=" ")
