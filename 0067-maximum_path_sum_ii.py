# -*- coding: utf-8 -*-
"""
Project Euler Problem N

Title:
Maximum path sum II

Description:
By starting at the top of the triangle below and moving to adjacent numbers on 
the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 
'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible 
to try every route to solve this problem, as there are 299 altogether! If you 
could check one trillion (1012) routes every second it would take over twenty 
billion years to check them all. There is an efficient algorithm to solve it. 
;o)

Solution:
Dynamic programming

Answer: 7273
I'm the 60,241st  person to solve this problem.

"""
with open('assets/p067_triangle.txt', 'r') as f:
    triangle = f.read()
f.closed

rows = triangle.split("\n")
rows_len = len(rows)
columns_len = len(rows[rows_len-1].split(" "))

matrix = [[None for x in xrange(columns_len)] for x in xrange(rows_len)]

for row_index, row_value in enumerate(rows):
    row_columns = rows[row_index].split(" ")

    for column_index, column_value in enumerate(row_columns):
        matrix[row_index][column_index] = int(row_columns[column_index])

for i in range(rows_len-1, -1, -1):
    
    for j in range(0, columns_len, 1):
        
        if i == 0:
            print matrix[i][j]
            break
        
        if matrix[i][j] is None or j + 1 == columns_len or matrix[i-1][j] is None:
            continue
        
        a = matrix[i][j] + matrix[i-1][j] 
        b = matrix[i][j+1] + matrix[i-1][j]
        
        if a > b:
            matrix[i-1][j] = a
        else:
            matrix[i-1][j] = b
