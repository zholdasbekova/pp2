import re

pattern = re.compile(r'[a-z]+_[a-z]+')

def find_sequences(s):
    return pattern.findall(s)

print(find_sequences("hello_world_foo_bar"))    
print(find_sequences("snake_caseCamelCase"))   
