from functools import reduce

def multiply_numbers(numbers):
    if not numbers:
        return None
    return reduce(lambda x, y: x * y, numbers)

numbers_list = [1, 2, 3, 4, 5]
result = multiply_numbers(numbers_list)
print("Result of multiplying all numbers in the list:", result)