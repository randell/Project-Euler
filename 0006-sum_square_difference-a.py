"""
Project Euler Problem 6

Title:
Sum square difference

Description:
The sum of the squares of the first ten natural numbers is, 
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is, 
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural 
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.

Solution:
Prepare functions for getting the sum of squares and square of sums and get the 
difference between the two.

Idea for solution B is to get the pattern of the differences.

Answer: 25164150
I'm the 189786th person to solve this problem.

"""
MIN = 1
MAX = 100

numbers = list(xrange(MIN, MAX+1))
print numbers


def sum_of_squares(numbers):
    return sum([i * i for i in numbers])


def square_of_the_sum(numbers):
    sum_of_numbers = sum(numbers)
    return sum_of_numbers * sum_of_numbers


def difference_of_sum_of_squares_and_square_of_sum(numbers):
    return square_of_the_sum(numbers) - sum_of_squares(numbers)

print difference_of_sum_of_squares_and_square_of_sum(numbers)