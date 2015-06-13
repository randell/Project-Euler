"""
Project Euler Problem 10

Title:
Summation of primes

Description:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Solution:
Just sum up all the primes below two million.

Answer: 142913828922
I'm the 129,964th person to solve this problem.
Earned Decathlete: Solve ten consecutive problems

"""
from lib.util import *

x = 2000000


def sum_of_primes_below(x):
    sum = 0

    for i in range(2, x):
        if is_prime(i):
            sum += i

    return sum

print sum_of_primes_below(x)