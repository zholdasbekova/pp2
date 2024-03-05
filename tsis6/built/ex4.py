import time
import math

def sq_milli(number, milliseconds):
    time.sleep(milliseconds / 1000)
    return math.sqrt(number)

number = 25100
milliseconds = 2123
result = sq_milli(number, milliseconds)
print(f"Square root of {number} after {milliseconds} milliseconds is {result}")
