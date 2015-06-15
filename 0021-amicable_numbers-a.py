# -*- coding: utf-8 -*-
"""
Project Euler Problem 21

Title:
Amicable numbers

Description:
Let d(n) be defined as the sum of proper divisors of n (numbers less than n 
which divide evenly into n). If d(a) = b and d(b) = a, where a ≠ b, then a and b 
are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

Solution:
Prepare a function for getting the proper divisors.

Answer: 31626
I'm the 62,615th person to solve this problem.

"""
limit = 10000


def proper_divisors(x):
    pd = []

    if x > 0:
        pd.append(1)

    i = 2

    while True:
        if i in pd:
            continue

        if x % i == 0:
            divisor = x / i

            if i not in pd:
                pd.append(i)

            if divisor not in pd:
                pd.append(divisor)

        i += 1

        if i * i >= x:
            break

    return pd


i = 2
amicable_numbers = []

while True:
    x = sum(proper_divisors(i))
    y = sum(proper_divisors(x))
    z = sum(proper_divisors(y))

    if i == y and x == z and i != x:
        if i not in amicable_numbers:
            amicable_numbers.append(i)

        if x not in amicable_numbers:
            amicable_numbers.append(x)

    i += 1

    if i >= limit:
        break

print amicable_numbers
print sum(amicable_numbers)