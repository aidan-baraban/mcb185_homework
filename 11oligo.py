# A function that returns the oligo melting temperature, depending on nt numbers

def melting_temp(A, T, G, C):
    total = A + T + G + C
    
    if total <= 13:
        Tm = (A + T) * 2 + (G + C) * 4
    else:
        Tm = 64.9 + (41 * (G + C - 16.4)) / (total)
    return Tm
    
print(melting_temp(5, 7, 3, 4))
print(melting_temp(2, 4, 1, 0))