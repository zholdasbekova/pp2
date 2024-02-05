def unique_elements(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

user_input = input("Enter a list of elements separated by spaces: ")
input_list = [int(item) for item in user_input.split()]
result = unique_elements(input_list)
print("Original list:", input_list)
print("List with unique elements:", result)
