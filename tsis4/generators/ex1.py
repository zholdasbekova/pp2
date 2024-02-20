#square
def squares_generator(N):
    for i in range(N):
        yield i ** 2

N = int(input("Enter a number: "))
for square in squares_generator(N):
    print(square, end=" ")


#evennumbers
def even_numbers_generator(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a number: "))
even_numbers = even_numbers_generator(n)
print(','.join(map(str, even_numbers)))


#divisibleby3and4
def divisible_by_3_and_4(start, end):
    for i in range(start, end+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
for num in divisible_by_3_and_4(start, end):
    print(num, end=" ")
