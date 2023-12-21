n = int(input('Input number >>> '))
n_len = n

for n in range(n):
    string = '1' + ('0' * n)
    print(("%.0f" % (n)).rjust(2), string.rjust(n_len))
