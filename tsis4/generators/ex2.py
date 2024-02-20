#squarestoyeild
def squares(a, b):
    for i in range(a, b+1):
        yield i ** 2

a = int(input("Enter the starting number: "))
b = int(input("Enter the ending number: "))
for square in squares(a, b):
    print(square)
    
 
#return0
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

# Test the generator
n = int(input("Enter a number: "))
for num in countdown(n):
    print(num, end=" ")   