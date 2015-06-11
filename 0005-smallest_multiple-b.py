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
Utilize the LCM of the divisors. 

Answer: 232792560
I'm the 187,747th person to solve this problem.

"""
from lib.util import *

MIN_DIVISOR = 2
MAX_DIVISOR = 20

# Range as defined by the problem
divisors = list(xrange(MIN_DIVISOR, MAX_DIVISOR))

# Set of prime numbers from each prime factorization set with the highest
# exponent value
largest_prime_factors = {}

# Starting point for multiplying everything later
smallest_multiple = 1


def prime_factors(x):
    """
    Returns {x1: y1, x2: y2, x3: y3..., xN: yN} where x is the prime factor, and
    y is the exponent value. 
    
    Prime factorization of 12 = 2 * 2 * 3 = 2^2 * 3^1 * 5^0
    prime_factors(12) will return {2: 2, 3: 1, 5: 0} 
    """
    prime_factors = {}
    
    # Start with the lowest possible prime number
    i = 2
    z = x

    if is_prime(x):
        # If x is prime, then its only prime factor is itself.
        return {x: 1}

    while True:
        # Skip numbers that are not prime.
        if not is_prime(i):
            i += 1
            continue

        # Check if prime number divides z without a remainder.
        if 0 == (z % i):
            # We count how many times z can be divided by i perfectly.
            prime_factors[i] = 1 if i not in prime_factors else prime_factors[i] + 1
            
            # Re-assign the new value of z after diving perfectly with i.
            z /= i
        else:
            i += 1

        if i > x / 2:
            break

    return prime_factors

for i in divisors:
    i_prime_factors = prime_factors(i)

    for j in i_prime_factors:
        # We only want the prime factors from each set with the highest exponent
        # value
        if j not in largest_prime_factors or largest_prime_factors[j] < i_prime_factors[j]:
            largest_prime_factors[j] = i_prime_factors[j]

# Using the set of prime numbers with the highest value, get the least common
# multiple
for i in largest_prime_factors:
    smallest_multiple *= (i ** largest_prime_factors[i])

print str(smallest_multiple)



