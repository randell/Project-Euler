"""
Project Euler Problem 1

Title:
Multiples of 3 or 5

Description:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 
3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Solution:
This version is a naive implementation using a loop and modulus division.

Answer: 233168.
I'm the 311384th person to solve this problem.
"""
sum = 0

for x in range(0, 10):
    sum += x if x % 3 == 0 or x % 5 == 0 else 0

print sum