"""
Project Euler Problem 16

Title:
Power digit sum

Description:
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

Solution:
Get the power then add the digits.

Answer: 1366
I'm the 98382nd person to solve this problem.

"""
power = 1000


def power_digit(x):
    return 2 ** x


def digit_sum(x):
    str_x = str(x)
    sum = 0

    for i in str_x:
        sum += int(i)

    return sum

print digit_sum(power_digit(power))