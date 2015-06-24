# -*- coding: utf-8 -*-
"""
Project Euler Problem N

Title:
Non-abundant sums

Description:
A perfect number is a number for which the sum of its proper divisors is exactly 
equal to the number. For example, the sum of the proper divisors of 28 would be 
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n 
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest 
number that can be written as the sum of two abundant numbers is 24. By 
mathematical analysis, it can be shown that all integers greater than 28123 can 
be written as the sum of two abundant numbers. However, this upper limit cannot 
be reduced any further by analysis even though it is known that the greatest 
number that cannot be expressed as the sum of two abundant numbers is less than 
this limit.

Find the sum of all the positive integers which cannot be written as the sum of 
two abundant numbers.

Solution:


Answer:
I'm the Nth person to solve this problem.

"""
from lib.util import *

abundant_numbers = {}

def is_abundant(x):
    
    if x in abundant_numbers and abundant_numbers[x]:
        return True
    
    if sum(proper_divisors(x)) > x:
        abundant_numbers[x] = True
        
        return abundant_numbers[x]
    
    abundant_numbers[x] = False
    
    return False

def is_sum_of_two_abundant_numbers(x):
    for i in range(12, x/2+1):
        if is_abundant(i) and is_abundant(x-i):
            return True
    
    return False

sum_of_two_abundants = []
not_sum_of_two_abundants = []
abundant_limit = 28124
lower_limit = 1
upper_limit = abundant_limit

for x in range(lower_limit, upper_limit):
     
    if is_sum_of_two_abundant_numbers(x):
        sum_of_two_abundants.append(x)
        continue
    
    not_sum_of_two_abundants.append(x)

import pprint 
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(abundant_numbers)

print sum_of_two_abundants
print sum(sum_of_two_abundants)
print not_sum_of_two_abundants
print sum(not_sum_of_two_abundants)