def count_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return len(lines)

filename = "example.txt"
print("Number of lines:", count_lines(filename))
