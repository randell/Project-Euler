# -*- coding: utf-8 -*-
"""
Project Euler Problem 15

Title:
Lattice paths

Description:
Starting in the top left corner of a 2×2 grid, and only being able to move to 
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

Solution:
Add the path count of the (top and left) nodes going to the current node.

Answer: 137846528820
I'm the 77,187th person to solve this problem.

"""
rows_len = 21
columns_len = 21

matrix = [[0 for x in xrange(columns_len)] for x in xrange(rows_len)]
matrix[0][0] = 1


def get_top_cell_value(row, column):
    row_minus_one = row - 1

    return matrix[row_minus_one][column]


def get_left_cell_value(row, column):
    column_minus_one = column - 1

    return matrix[row][column_minus_one]


def set_cell_value(row, column, value):
    matrix[row][column] = value


def get_cell_value(row, column):
    cell_value = 1

    if row > 0 and column > 0:
        cell_value = get_left_cell_value(row, column) + get_top_cell_value(row, column)
        set_cell_value(row, column, cell_value)

        return cell_value

    set_cell_value(row, column, cell_value)

    return cell_value

print("")

for i in range(0, rows_len):
    for j in range(0, columns_len):
        print "%4d" % get_cell_value(i, j),

    print("")