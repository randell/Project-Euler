"""
Project Euler Problem N

Title:
Special Pythagorean triplet

Description:
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, 
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Solution:
Loop through the list of a's, b's, and c's that sum up to 1000 while checking 
which combination will give a^2 + b^2 = c^2.

Answer: 31875000
I'm the 142,366th person to solve this problem.

"""
abc = []
sum = 1000


for a in range(1, 999):
    for b in range(1, 999):
        c = sum - a - b

        if a * a + b * b == c * c:
            product = a * b * c
            break

print product