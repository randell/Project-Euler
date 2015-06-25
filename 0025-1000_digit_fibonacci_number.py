# -*- coding: utf-8 -*-
"""
Project Euler Problem N

Title:
1000-digit Fibonacci number

Description:
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 
digits?

Solution:


Answer: 4782
I'm the 92,572nd  person to solve this problem.

Nice work, randell.benavidez, you've just advanced to Level 1.
72997 members (14.62%) have made it this far.

You have earned 1 new award:

The Journey Begins: Progress to Level 1 by solving twenty-five problems

"""
a = 1
b = 1
c = 0
counter = 2
digits = 1000

while True:
    counter += 1
    c = a + b

    a = b
    b = c
    
    if len(str(c)) == 1000:
        print counter
        break