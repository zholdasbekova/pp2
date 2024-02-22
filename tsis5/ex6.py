import re

def replace_chars(s):
    return re.sub(r'[ ,.]', ':', s)

print(replace_chars("a, b. c d e"))   
