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
print(type(a), type(b), type(c), sep=', ', end='?\n')

# functions

def pythagoras(a, b): return math.sqrt(a**2 + b**2)
print(pythagoras(3, 4))

r = 4
w = 6
h = 7


def circle_area(r): return math.pi * r**2 # calculate the area of a circle
print(circle_area(r))

def rectangle_area(w, h): return w * h # calculate the area of a rectangle

def FtoC(f): return ((f-32)*5)/9 # convert Fahrenheit to Celsius
print(FtoC(98.6))

def CtoF(c): return (c*(9/5)+32) # convert Celsius to Fahrenheit
print(CtoF(37))


def mphtokph(m): return (m*1.60934) # convert mph to kph
print(mphtokph(15))

def kphtomph(k): return (k/1.60934) # convert kph to mph
print(kphtomph(24.1401))

def compute_dna_conc(od260, dilution_factor=1): # compute DNA conc. from OD260 with any dilution factor (default=1)
    dna_conc = od260 * dilution_factor * 50
    return dna_conc
print(compute_dna_conc(od260=0.8,dilution_factor=10))

s = 'hello world'
print(s, type(s))

a = 2
b = 3
if a == b: # conditional statement
    print('a equals b')
print(a, b)

def is_even(x):       #check if number is evenly divisible by 2
    if x % 2 == 0: return True
    return False
    
print(is_even(2))
print(is_even(3))

c = a == b
print(c)
print(type(c))

### if-elif-else

if   a < b: print('a < b')
elif a > b: print('a > b')
else:       print('a == b')


def silly(m, x, b): y = m *x + b ## None Type (no return function)
print(silly(2, 3, 4))

## More Practice
x = 3.45

def is_integer(x):    # check if a number is an integer
    return x % 1 == 0 # if remainder is 0 when divided by 1, it is an integer

print(is_integer(5))
print(is_integer(5.6))

def is_probability(x):      # check if number is valid probability
    return 0 <= x <= 1
    
print(is_probability(-0.5))
print(is_probability(0.7))

def molecular_weight_DNA(letter):  # return molecular weight of DNA letter, if not a nucleotide then return None
    if letter == 'A':
        return 313.2
    if letter == 'T':
        return 304.2
    if letter == 'C':
        return 289.2
    if letter == 'G':
        return 329.2
    return None
print(molecular_weight_DNA('A'))
print(molecular_weight_DNA('K'))

def return_complement(letter):  # returns complement of DNA letter, returning None if it isn't a nucleotide
    if letter == 'A':
        return 'T'
    if letter == 'T':
        return 'A'
    if letter == 'C':
        return 'G'
    if letter == 'G':
        return 'C'
    return None

print(return_complement('T'))
print(return_complement('X'))

## Even More Practice

def three_max(a, b, c):
    max_value = a           # assumption that a is initially the max
    if b > max_value:
        max_value = b       # max_value is now b, if it is larger
    if c > max_value:
        max_value = c
    return max_value

print(three_max(15, 45, 76))
print(three_max(500, 7, 8))


def sensitivity(tp, fn):       # true positive, false negatives
    return tp / (tp+fn)

def specificity(tn, fp):       # true negative, false positive
    return tn / (tn+fp)

def f1_score(tp, fp):          # true positive, false prositive
    return tp / (tp+fp)

print(sensitivity(50, 4))
print(specificity(70, 10))
print(f1_score(50, 10))


def shannon_entropy(A, C, G, T):
    total = A + C + G + T
    if total == 0:
        return 0.0
    
    prob_A = A / total
    prob_C = C / total
    prob_G = G / total
    prob_T = T / total
    entropy = 0.0
    
    if prob_A > 0:
        entropy -= prob_A * math.log2(prob_A)
    if prob_C > 0:
        entropy -= prob_C * math.log2(prob_C)
    if prob_G > 0:
        entropy -= prob_G * math.log2(prob_G)
    if prob_T > 0:
        entropy -= prob_T * math.log2(prob_T)
    return entropy

print(shannon_entropy(25, 30, 0, 8))
print(shannon_entropy(50, 55, 88, 120))