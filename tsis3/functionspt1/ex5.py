from itertools import permutations

def print_permutations(input_string):
    perms = permutations(input_string)
    for perm in perms:
        print(''.join(perm))
user_input = input("Enter a string: ")
print_permutations(user_input)