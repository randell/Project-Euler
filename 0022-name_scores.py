# -*- coding: utf-8 -*-
"""
Project Euler Problem N

Title:
Name scores

Description:
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file 
containing over five-thousand first names, begin by sorting it into alphabetical 
order. Then working out the alphabetical value for each name, multiply this 
value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is 
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would 
obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file

Solution:


Answer: 871198282
I'm the 79,213th  person to solve this problem.

"""
with open('assets/p022_names.txt', 'r') as f:
    read_data = f.read()
f.closed

names = [x.strip('"') for x in read_data.split(",")]
names.sort()

alphabetical_value = {
                      'A': 1,
                      'B': 2,
                      'C': 3,
                      'D': 4,
                      'E': 5, 
                      'F': 6,
                      'G': 7,
                      'H': 8,
                      'I': 9,
                      'J': 10,
                      'K': 11,
                      'L': 12,
                      'M': 13,
                      'N': 14,
                      'O': 15,
                      'P': 16,
                      'Q': 17,
                      'R': 18,
                      'S': 19,
                      'T': 20,
                      'U': 21,
                      'V': 22,
                      'W': 23,
                      'X': 24,
                      'Y': 25,
                      'Z': 26
                      }

def get_name_score(str):
    name_score = 0
    
    for x in str:
        name_score += alphabetical_value[x]
        
    return name_score

total_name_score = 0;

for i, name in enumerate(names):
    name_score = get_name_score(name)
    multiplier = (i+1) 
     
    total_name_score += (get_name_score(name) * (i+1))

print total_name_score