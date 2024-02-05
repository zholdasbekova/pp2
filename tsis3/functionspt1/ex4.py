def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(number_list):
    return list(filter(is_prime, number_list))
user_input = input("Enter a list of numbers separated by spaces: ")
numbers = [int(num) for num in user_input.split()]
prime_numbers = filter_prime(numbers)

print("Original list:", numbers)
print("Prime numbers:", prime_numbers)