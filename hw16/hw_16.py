def num_or_not():
    """Function proceed exceptions. If at least one of two entered values
    is not a number, concatenation is done. In other case - sum"""
    try:
        # asking to enter 2 values
        value_1 = input("Enter first value >>> ")
        value_2 = input("Enter second value >>> ")

        # try to convert values to numbers
        num_1 = int(value_1)
        num_2 = int(value_2)

        # if both values are numbers - calculate sum of values
        return num_1 + num_2
    except ValueError:
        # if at least one of two entered values is not a number - concat
        return value_1 + value_2


# Check function work
result = num_or_not()
print(result)
