# -*- coding: utf-8 -*-
"""
Project Euler Problem 18

Title:
Maximum path I

Description:
By starting at the top of the triangle below and moving to adjacent numbers on 
the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

                           75
                         95 64
                       17 47 82
                     18 35 87 10
                   20 04 82 47 65
                  19 01 23 75 03 34
                88 02 77 73 07 63 67
              99 65 04 28 06 16 70 92
            41 41 26 56 83 40 80 70 33
          41 48 72 33 47 32 37 16 94 29
        53 71 44 65 25 43 91 52 97 51 14
      70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
  63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by 
trying every route. However, Problem 67, is the same challenge with a triangle 
containing one-hundred rows; it cannot be solved by brute force, and requires a 
clever method! ;o)

Solution:
Dynamic programming

Answer: 1074
I'm the 85,722nd  person to solve this problem.

"""
triangle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

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