"""
Project Euler Problem 1

Title:
Multiples of 3 or 5

Description:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Solution:
This version further simplifies getting the sum of an arithmetic series since we already know that the first element in
the series and the difference to the next element in the series are the same.

Answer: 233168.
I'm the 311384th person to solve this problem.

"""
count_multiples_of_3 = 999 / 3
count_multiples_of_5 = 999 / 5
count_multiples_of_15 = 999 / 15

def sum_of_arithmetic_series(n, a):
    return (a * n * (n + 1)) / 2

sum_3 = sum_of_arithmetic_series(count_multiples_of_3, 3)
sum_5 = sum_of_arithmetic_series(count_multiples_of_5, 5)
sum_15 = sum_of_arithmetic_series(count_multiples_of_15, 15)

print sum_3 + sum_5 - sum_15