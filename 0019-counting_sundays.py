# -*- coding: utf-8 -*-
"""
Project Euler Problem N

Title:
Counting Sundays

Description:
You are given the following information, but you may prefer to do some research 
for yourself.

- 1 Jan 1900 was a Monday.
- Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
- A leap year occurs on any year evenly divisible by 4, but not on a century 
unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 
Jan 1901 to 31 Dec 2000)?

Solution:
171

Answer:
I'm the 79,349th person to solve this problem.

"""
DAYS_IN_A_LEAP_YEAR = 366
DAYS_IN_A_YEAR = 365
DAYS_IN_A_WEEK = 7
DAYS_IN_JANUARY = 31

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_of_the_week = {
                    'Sunday': 0,
                    'Monday': 1,
                    'Tuesday': 2,
                    'Wednesday': 3,
                    'Thursday': 4,
                    'Friday': 5,
                    'Saturday': 6,
                    }

def is_leap_year(year):
    if year % 100 == 0 and year % 400 != 0:
        return False;
    
    if year % 4 == 0:
        return True
    
    return False

def get_days_in_the_year(year):
    if is_leap_year(year):
        return DAYS_IN_A_LEAP_YEAR

    return DAYS_IN_A_YEAR

running_days = get_days_in_the_year(1900)+1
first_of_the_month_sundays = 0

for x in range(1901, 2001):
    for y in month_days:
        if running_days % DAYS_IN_A_WEEK == days_of_the_week['Sunday']:
            first_of_the_month_sundays += 1
          
        running_days += y
    
print first_of_the_month_sundays