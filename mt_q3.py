#!/usr/bin/env python3

# program: mt_q3.py

# author_id: [seneca_id]

def greetings(time):
    hhmm = int(time.replace(':',''))
    greeting_message = ' '
    if hhmm < 1200:
       print("Good Morning")
    elif hhmm >= 1200:
       print("Good Day")
 
    return greeting_message

if __name__ == '__main__':
    time = input('What is the time in HH:MM? ')
    print('Hello,',greetings(time))