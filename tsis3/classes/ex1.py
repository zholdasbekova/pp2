class StringManipulator:
    def __init__(self):
        self.input_string = ""
    def getString(self):
        self.input_string = input("Enter string: ")
    def printString(self):
        print("Uppercase:", self.input_string.upper())


string_obj = StringManipulator()
string_obj.getString()
string_obj.printString()
