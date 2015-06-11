"""
Project Euler Problem 5

Title:
Smallest multiple

Description:
2520 is the smallest number that can be divided by each of the numbers from 1 to 
10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the 
numbers from 1 to 20?

Solution:
Increment x by 1 while checking if x is divisible by all of the divisors. This 
solution takes years to get the answer. Solution B will utilize the LCM of the 
divisors.

Answer: 232792560
I'm the 187,747th person to solve this problem.

"""
MIN_DIVISOR = 1
MAX_DIVISOR = 20

divisors = list(xrange(MIN_DIVISOR, MAX_DIVISOR))

def is_divisible_by_divisors(x):
    for i in divisors:
        if x % i != 0:
            return False

    return True

x = MAX_DIVISOR

while True:
    if is_divisible_by_divisors(x):
        break
    else:
        x += 1

print x
