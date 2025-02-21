# Phred quality functions but with 10 characters (A-J)
# char_to_prob
# prob_to_char


def char_to_prob(char):                         # convert quality score character A-J to probability (2^-n)
    return 2 ** -(ord(char) - ord('A') + 1)
    
print(char_to_prob('C'))


import math

def prob_to_char(prob):
    score = -math.log2(prob)
    return chr(round(score) + ord('A')-1)     
    
print(prob_to_char(0.125))