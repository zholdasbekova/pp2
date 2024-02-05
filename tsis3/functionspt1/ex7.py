def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

user_input = input("Enter a list of integers separated by spaces: ")
nums = [int(num) for num in user_input.split()]
result = has_33(nums)
print(f"The list {nums} contains a 3 next to a 3: {result}")