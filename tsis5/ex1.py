import re

pattern = re.compile(r'ab*')

def match_string(s):
    return bool(pattern.match(s))

print(match_string("ab"))    
print(match_string("abb"))   
print(match_string("ac"))    
