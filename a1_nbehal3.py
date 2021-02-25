#!/usr/bin/env python3

import os #This line imports the os module – which is a module used to interact with the operating system the python script is running on, it is only after we import this module that the functions defined below will work.
import sys #This imports the sys module which provides variables and functions used to manipulate the python environment and allows us to read what arguments are passed on onto the script on the command line – for example it is only after importing the sys module that arguments can be passed onto the script from cmd-line such as a1.py 2020 where a1.py can be denoted by sys.argv[0] and 2020 by sys.argv[1] where [n] is the command line index


def leap_year(year): 
    '''Takes in a year(4 digit int) as an argument and determines whether the year is a leap year or not
    Leap years repeat after every 4 years'''               
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)   
    
def sanitize(obj1,obj2):
    '''Takes 2 strings and replaces (difference in terms of sets) what is present in obj1 but
    not in obj2 with a whitespace (alias Removes)'''
    for c in obj1:
        if c not in obj2:
            obj1 = obj1.replace(c,'')
    return(obj1)

def size_check(obj, intobj):
    '''Takes in 2 arguments - one string and other integer against which the length of 
    the string is to be benchmarked.'''
    return len(str(obj)) == intobj

def range_check(obj,obj2):
    '''Takes in 2 arguments - one integer and another tuple(fixed list) and checks whether
    the given integer(obj1) is a part of the range defined by the tuple'''
    o_min = obj2[0]
    o_max = obj2[1]+1
    return obj in range(o_min,o_max)
    
def usage():
    '''Takes in no argument but prints how to use the script and what arguments to be
    supplied at the command line'''
    print('Usage: '+sys.argv[0]+' YYYYMMDD|YYYY/MM/DD|YYYY-MM-DD|YYYY.MM.DD')
    
if __name__ == '__main__':
    if len(sys.argv) !=2:
        usage()
        sys.exit()
    month_name = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                    7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    user_raw_data = sys.argv[1]
    allow_chars = '0123456789'
    dob = sanitize(user_raw_data, allow_chars)
    result = size_check(dob,8)
    if result == False:
        print("Error 09: wrong date entered")
        sys.exit()
    year = int(dob[0:4])
    month = int(dob[4:6])
    day = int(dob[6:])
        
    result = range_check(year,(1900,9999))
    if result == False:
        print("Error 10: year out of range, must be 1900 or later")
        sys.exit()
    result = range_check(month,(1,12))
    if result == False:
        print("Error 02: wrong month entered")
        sys.exit()
    result = leap_year(year)
    if result == True:
        days_in_month[2] = 29
    result = range_check(day, (1, days_in_month[month]))
    if result == False:
        print("Error 03: wrong day entered")
        sys.exit()
    else:
        new_dob = str(month_name[month - 1]+' '+str(day)+', '+str(year))
        print(new_dob)
            