# Write functions that convert quality value symbols into error rates and vice-versa.
# The ord() function returns the ASCII value of a letter.
# The chr() function turns an ASCII value into a letter.
# Demonstrate the functions work by calling them several times. Edge cases should return None.


import math

def char_to_prob(char):
    if not char:
        return None
      
     
    ascii_value = ord(char)                 # get ascii value
    if ascii_value < 33 or ascii_value > 126:
        return None
    
    if 33 <= ascii_value <= 126:            # ascii range for FASTQ quality characters
        phred_score = ascii_value - 33
        return 10 ** (-phred_score / 10)
    else:
        return None 
        
def prob_to_char(prob):
    if prob <= 0 or prob >= 1:              # not a valid probability, return None
        return None
        
    phred_score = -10 * math.log10(prob)
    ascii_value = phred_score + 33
    
    if ascii_value < 33 or ascii_value > 126:     # if out of FASTQ range, give None
        return None
    
    round_ascii_value = round(ascii_value)        # round to an integer
    if 33 <= ascii_value <= 126:
        return chr(round_ascii_value)             # convert ascii to character
    
    else:
        return None



print(char_to_prob('A'))
print(prob_to_char(0.001))
print(prob_to_char(1.5))
print(char_to_prob('>'))