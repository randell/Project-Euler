# -*- coding: utf-8 -*-
"""
Project Euler Problem N

Title:
Lexicographic permutations

Description:
A permutation is an ordered arrangement of objects. For example, 3124 is one 
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are 
listed numerically or alphabetically, we call it lexicographic order. The 
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 
6, 7, 8 and 9?

Solution:


Answer: 2783915460
I'm the 68,481st person to solve this problem.

You have earned 1 new award:

Easy Prey: Solve twenty-five of the fifty easiest problems

"""
digits = sorted([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
digits_len = len(digits)
permutations = []
counter

while True:
    perms = permutations
    new_perms = []
    
    if len(permutations) != 0:
        for p in perms:
            for x in digits:
                if x not in p:
                    new_perms.append(p + [x])
            
    else:
        for x in digits:
            new_perms.append([x])
    
    permutations = new_perms
    
    if len(new_perms[0]) == digits_len:
        break

print "".join(str(x) for x in permutations[999999])