# 1. Write a function that computes the distance between 2 points in a graph

import math

def compute_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

a = (4, 5)
b = (2, 9)

print(compute_distance(a, b))

# 2. Return complement of a DNA letter, return None if the letter isn't DNA

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

# 3. Write a function max3() that returns the maximum of 3 numbers

def max3(a, b, c):
    max_value = a
    
    if b > max_value:
        max_value = b
    if c > max_value:
        max_value = c
    return max_value

print(max3(9, 8, 7))
print(max3(15, 16, 20))

# 4. Why do you think PHRED quality values are -10*log10 rather than -log2?
# How would you modify your program if you thought log2 was better?

# Bioinformatics tools tend to use the log10 scale, so changing it to log2 here would
# make comparisons impossible, since the scale used to calculate your values would
# be different. The only changes to the program might be altered function titles like
# char_to_prob_log2 and then actually going into the formula and changing it to
# 2 ** (-phred_score / 10) and then for prob_to_char_log2, it would be changed to 
# -mathlog2(prob).