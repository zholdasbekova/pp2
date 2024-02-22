import re

pattern = re.compile(r'a.*b$')

def match_string(s):
    return bool(pattern.match(s))

print(match_string("acb"))    
print(match_string("ab"))     
print(match_string("aanythingb"))   
