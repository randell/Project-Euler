"""
Project Euler Problem 7

Title:
10001st prime

Description:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that 
the 6th prime is 13.

What is the 10001st prime number?

Solution:
Just run through all the numbers until we get the Nth prime.

Answer: 104743
I'm the 161,534th person to solve this problem.

"""
from lib.util import *

n = 10001


def nth_prime(n):
    counter = 0
    i = 2

    while True:
        if is_prime(i):
            counter += 1

        if n == counter:
            break

        i += 1

    return i

print nth_prime(n)