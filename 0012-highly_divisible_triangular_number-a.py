"""
Project Euler Problem 12

Title:
Highly divisible triangular number

Description:
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be
1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?

Solution:
Define functions for getting triangle numbers and another function for counting the factors of triangle numbers. Loop
until 500 divisor-triangle number is reached.

Answer: 76576500
I'm the 87663rd person to solve this problem.

"""
divisors = 500


def triangle_number(x):
    sum = 0

    for i in range(x + 1):
        sum += i

    return sum


def count_factors(x):
    counter = 0
    i = 1

    while True:
        if x % i == 0:
            counter += 1

            quotient = x/i

            if i != quotient:
                counter += 1

        i += 1

        if i * i > x:
            # If we reach the square root of a number and we still cannot find a divisor, it's prime. No need to divide
            # using the remaining numbers.
            break

    return counter

i = 1

while True:
    tn = triangle_number(i)

    if count_factors(tn) >= divisors:
        break

    i += 1

print tn