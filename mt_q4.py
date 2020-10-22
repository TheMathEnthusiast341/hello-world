#!/usr/bin/env python3

# program: mt_q4.py

# author_id: nbehal3

def mark2grade(number):
    mark = int(number)
    if 90 <= mark <= 100: return "A"
    elif 80 <= mark <= 99: return "B"
    elif 70 <= mark <= 79: return "C"
    elif 60 <= mark <= 69: return "D"
    elif 0 <= mark <= 59: return "F"
    
    # insert code below to convert marks to letter grades,
    # do not add any extra return statement
    if mark < 0:
        grade = 'Invalid'
    # insert your code here
    return grade

if __name__ == '__main__':
    raw_mark = input('Please enter a mark (0-100): ')
    print('Your grade is',mark2grade(raw_mark)+'.')