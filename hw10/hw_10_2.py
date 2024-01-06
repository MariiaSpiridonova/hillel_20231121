import random
from tabulate import tabulate


def create_matrix(*params):
    """function should create 2d list with given params of
    number of lists and number of elements in the list.
    Can have no params, only 1 param and 2 params.
    All elements - numbers from 0 to 200"""
    if len(params) == 0:
        return 'Sorry, no params - no table'
    elif len(params) == 1:
        return [[random.randint(0, 200) for i in range(params[0])]
                for j in range(params[0])]
    elif len(params) == 2:
        return [[random.randint(0, 200) for i in range(params[0])]
                for j in range(params[1])]


def check_matrix_symetry(d2_list):
    """function checks matrix and print it if symmetrical"""
    num_rows = len(d2_list)
    num_elements = len(d2_list[0])
    if num_rows == num_elements:
        return d2_list


print(f'\n{create_matrix()}\n')
print(tabulate(check_matrix_symetry(create_matrix(5, ))))
print(tabulate(create_matrix(3, 7)))
