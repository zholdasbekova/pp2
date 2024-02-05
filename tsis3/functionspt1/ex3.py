def solve(num_heads, num_legs):
    if num_heads < 0 or num_legs < 0 or num_legs % 2 != 0:
        return None, None
    num_rabbits = (num_legs - 2 * num_heads) / 2
    num_chickens = num_heads - num_rabbits
    if num_rabbits >= 0 and num_chickens >= 0 and num_rabbits.is_integer() and num_chickens.is_integer():
        return int(num_rabbits), int(num_chickens)
    else:
        return None, None

num_heads_input = int(input("Enter the number of heads: "))
num_legs_input = int(input("Enter the number of legs: "))

rabbits, chickens = solve(num_heads_input, num_legs_input)
if rabbits is not None and chickens is not None:
    print(f"The number of rabbits is: {rabbits}")
    print(f"The number of chickens is: {chickens}")
else:
    print("Invalid input. Please provide non-negative integers for the number of heads and legs.")