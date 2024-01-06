def check_sum_of_pair(numbers_list, target_sum):
    """function accepts as params a list of numbers (various length)
    and single number and checks if sum of any two numbers
    from the list equals the given single number"""
    checked = set()
    for number in numbers_list:
        complement = target_sum - number
        if complement in checked:
            return True
        checked.add(number)
    return False


print(check_sum_of_pair([4, 5, 6, 7, 8], 16))
print(check_sum_of_pair([4, 5, 6, 7, 8, 9], 16))
