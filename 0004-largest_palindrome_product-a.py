"""
Project Euler Problem 4

Title:
Largest palindrome product

Description:
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Solution:
Prepare a function to check for numeric palindromes. Use it to check for palindrome products of 3 digit numbers while
keeping track of the largest palindrome value.

Answer: 906609
I'm the 172039th person to solve this problem.

"""
from lib.util import *

MIN = 100
MAX = 999


def get_largest_palindrome_product(x):
    largest = -1

    for i in range(MIN, MAX):
        for j in range(MIN, MAX):
            product = i * j

            if is_palindrome(product):
                largest = product if product > largest else largest

    return largest

print get_largest_palindrome_product(MAX)