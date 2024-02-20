def spy_game(nums):
    nums_str = ''.join(map(str, nums))
    return '007' in nums_str

user_input = input("Enter a list of integers separated by spaces: ")
nums = [str(num) for num in user_input.split()]
result = spy_game(nums)
print(f"The list {nums} contains '007' in order: {result}")
