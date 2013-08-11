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
I'm the 188047th person to solve this problem.

"""
def is_prime(x):
    """
    Checks if a given number is prime
    """
    is_prime = True

    # If the number is 2 or 3, we don't even need to compute if it's prime.
    if x <= 3:
        return is_prime

    # We check if the number is divisible by a certain number, starting with 2.
    i = 2

    while True:
        if x % i == 0:
            # If the number is divisible by a another number except for 1 and itself, it's composite (not prime).
            return False

        i += 1

        if i * i > x:
            # If we reach the square root of a number and we still cannot find a divisor, it's prime. No need to divide
            # using the remaining numbers.
            break

    return is_prime


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