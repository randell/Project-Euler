# -*- coding: utf-8 -*-
"""
Project Euler Problem 20

Title:
Factorial digit sum

Description:
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

Solution:
Create a factorial function. Use our digit_sum function created for Problem 16: 
Power digit sum.

Answer: 648
I'm the 91495th person to solve this problem.

"""
from lib.util import *

x = 100


print digit_sum(factorial(x))
