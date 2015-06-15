# -*- coding: utf-8 -*-
"""
Project Euler Problem 17

Title:
Number letter counts

Description:
If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in 
words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 
letters. The use of "and" when writing out numbers is in compliance with British 
usage.

Solution:


Answer: 21124
I'm the 64064th person to solve this problem.

"""
number_word = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand"
}


def get_ones(x):
    return "-" + number_word[int(x)] if x != "0" else ""

def number_to_words(x):
    word = ""

    if x <= 20:
        return number_word[x]

    if x < 100:
        x = str(x)

        tens = x[0]
        ones = get_ones(x[1])

        return number_word[int(tens) * 10] + ones

    if x < 1000:
        x = str(x)

        hundreds = number_word[int(x[0])] + " hundred"
        and_ = " and " if x[1] != "0" or x[2] != "0" else ""

        tens_ones_int = int(x[1] + x[2])

        if tens_ones_int == 0:
            tens_ones = ""
        elif tens_ones_int <= 20:
            tens_ones = number_word[tens_ones_int]
        else:
            tens = number_word[int(x[1]) * 10]
            ones = get_ones(x[2])

            tens_ones = tens + ones

        return hundreds + and_ + tens_ones

    if x == 1000:
        return "one thousand"

    return word


def phrase_length(x):
    return len(x.replace(" ", "").replace("-", ""))


words_length = 0

for i in range(1, 1001):
    print "i: " + str(i) + ", [" + str(number_to_words(i)) + "], " + str(phrase_length(number_to_words(i)))
    words_length += phrase_length(number_to_words(i))

print words_length