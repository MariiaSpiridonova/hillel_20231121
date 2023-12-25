import random

generated_list = [random.randint(1, 99) for i in range(15)]
print(generated_list)

sum_even = 0
sum_odd = 0

for i in generated_list:
    if (i % 2) == 0:
        sum_even += i
    else:
        sum_odd += i

if sum_odd > sum_even:
    print('Yes')
else:
    print('No')
