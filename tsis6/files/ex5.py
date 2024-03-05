def write_list_to_file(filename, input_list):
    with open(filename, 'w') as file:
        for item in input_list:
            file.write("%s\n" % item)


filename = "output.txt"
my_list = ["apple", "banana", "cherry"]
write_list_to_file(filename, my_list)
