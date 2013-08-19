"""
Project Euler Problem 5

Title:
Smallest multiple

Description:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Solution:
Utilize the LCM of the divisors.

Answer: 232792560
I'm the 187747th person to solve this problem.

"""
from lib.util import *

MIN_DIVISOR = 2
MAX_DIVISOR = 20

divisors = list(xrange(MIN_DIVISOR, MAX_DIVISOR))
largest_prime_factors = {}
smallest_multiple = 1


def prime_factors(x):
    prime_factors = {}
    i = 2
    z = x

    if is_prime(x):
        return {x: 1}

    while True:
        if not is_prime(i):
            i += 1
            continue

        y = z % i

        if 0 == y:
            prime_factors[i] = 1 if i not in prime_factors else prime_factors[i] + 1
            z /= i
        else:
            i += 1

        if i > x / 2:
            break

    return prime_factors

for i in divisors:
    i_prime_factors = prime_factors(i)

    for j in i_prime_factors:
        if j not in largest_prime_factors or largest_prime_factors[j] < i_prime_factors[j]:
            largest_prime_factors[j] = i_prime_factors[j]

for i in largest_prime_factors:
    smallest_multiple *= (i ** largest_prime_factors[i])

print str(smallest_multiple)



