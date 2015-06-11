"""
Project Euler Problem 3

Title:
Largest prime factor

Description:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Solution:
Create a function to check if a number is prime, then use this function to check if the factors if the given number are
primes, while keeping track of the largest one. We set the number itself as the largest prime factor in case we don't
find any other factors.

Answer: 6857
I'm the 188,047th person to solve this problem.

"""
from lib.util import *


def get_largest_prime_factor(x):
    largest_prime_factor = x
    i = 2

    while True:
        if x % i == 0 and is_prime(i):
            largest_prime_factor = i

        i += 1

        if i * i > x:
            # If we reach the square root of a number and we still cannot find a divisor, it's prime. No need to divide
            # using the remaining numbers.
            break

    return largest_prime_factor

print get_largest_prime_factor(600851475143)