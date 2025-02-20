## For Exam 2, write a program which identifies prime numbers and puts a star next to each,
## in a descending list from 51.


def prime(n):                               # identifies prime numbers
    for den in range(2, n//2, + 1):
        if n % den == 0: return False
    return True
  
    
for number in range(51, 0, -1):             # lists integers from 51 descending, with a star on prime numbers
    if prime(number):
        print(number, "*", sep="")          # no space b/t number and star
    else:
        print(number)