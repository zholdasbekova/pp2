import re

pattern = re.compile(r'[A-Z][a-z]+')

def find_sequences(s):
    return pattern.findall(s)


print(find_sequences("CamelCase snake_case"))  
