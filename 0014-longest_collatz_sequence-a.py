# -*- coding: utf-8 -*-
"""
Project Euler Problem 14

Title:
Longest Collatz sequence

Description:
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been
proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

Solution:
Prepare a function to determine the Collatz sequence length of x. Loop up to just under one million until we find the
longest chain.

Answer: 837799
I'm the 92318th person to solve this problem.

"""


def collatz_sequence_length(x):
    chain = [x]

    while True:
        if x % 2 == 0:
            x /= 2
        else:
            x = 3 * x + 1

        chain.append(x)

        if 1 == x:
            break

    return len(chain)

longest_chain = 0
longest_chain_starting_number = 0
i = 1

while True:
    csl = collatz_sequence_length(i)

    if csl > longest_chain:
        longest_chain = csl
        longest_chain_starting_number = i

    i += 1

    if 1000000 == i:
        break

print longest_chain_starting_number