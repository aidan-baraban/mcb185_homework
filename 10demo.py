# 10demo.py by aidan_baraban

print('hello, again') # greeting

"""
This is a
multi-line
comment!
"""

print(1.5e-2)
print(3 + 45)
print(4*(6+3))
print(2 * (5 % 2))

# trying out importing math

import math
print(math.log(146))
print(math.pow(10, 2))

# assigning variables

a = 3                      # one side of a triangle
b = 4                      # another side of a triangle
c = math.sqrt(a**2 + b**2) # hypotenuse
print(c)
print(type(a), type(b), type(c), sep=', ', end='!\n')

# functions

def pythagoras(a, b): return math.sqrt(a**2 + b**2)

print(pythagoras(3, 4))