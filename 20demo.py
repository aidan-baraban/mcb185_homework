## Tuples

t = 1, 2                            # this is a tuple
print(t)
print(type(t))

person = 'Steve', 21, 57891.50      # name, age, yearly income
print(person)
print(type(person))

def midpoint(x1, y1, x2, y2):       # return the midpoint of a line as a tuple
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y

print(midpoint(1, 2, 3, 4))         # calls the midpoint() function, output sent to print()
m = midpoint(1, 2, 3, 4)            # assigns variable m to return the value of the midpoint() function
mx, my = midpoint(1, 2, 3, 4)       # "unpacks" the tuple. the caller knows that the function returns two values, so the caller provides 2 variables, mx, and my
print(mx, my)                       # prints the separate values

print(m[0], m[1])                   # each item in a tuple gets a numeric index


## Iteration

# while

i = 0
while True:
    i = i + 1
    print('hey', i)
    if i == 3: break

i = 0
while i < 3:
    i = i + 1
    print('hey', i)

i = 1
while i < 10:
    print(i)
    i = i + 3
print('final value of i is', i)

# for i in range()

for i in range(1, 10, 3):
    print(i)

# for i in range(0, 5):
    print(i)
    
for i in range(5):
    print(i)
    
# for i in range(5): print(i)
# for i in range(0,5): print(i)
# for i in range(0, 5, 1): print(i)

for i in range(4, -1, -1): print(i)

# for item in container

basket = 'milk', 'eggs', 'bread'
for thing in basket:
    print(thing)
    
for i in range(len(basket)):
    print(basket[i])
    
## Nesting

for i in range(7):
    if i % 2 == 0: print(i, 'is even')
    else:          print(i, 'is odd')

## Practice Problems

def triangular(n):
    tria = 0
    for i in range(n+1):
        tria = tria + 1
    return tria

print(triangular(6))
print(triangular(2))

def factorial(n):
    if n == 0: return 1
    fac = 1
    for i in range(1, n + 1):
        fac = fac * i
    return fac
    
print(factorial(7))
print(factorial(19))

import math

def poisson(n, k):
    return n**k * math.e**-n / factorial(k)
    
print(poisson(3, 4))
print(poisson(8, 11))

def nchoosek(n, k):
    return factorial(n) / (factorial(k) * factorial(n-k))
    
print(nchoosek(2, 5))

def euler(limit):
    e = 0
    for n in range(limit):
        e = e + 1 / factorial(n)
    return e
    
print(euler(1000))

def prime(n):
    for den in range(2, n//2, + 1):
        if n % den == 0: return False
    return True
    
print(prime(47))

def nilakantha(limit):
    pi = 3
    for i in range(1, limit+1):
        n = 2 * i
        d = n * (n+1) * (n+2)
        if i % 2 ==0: pi = pi - 4 / d
        else:         pi = pi + 4 / d 
    return pi

print(nilakantha(50))

print('RandomNumbers')

## Random Numbers

import random

for i in range(5):
    print(random.random())
    
for i in range(3):
    print(random.randint(1, 6))