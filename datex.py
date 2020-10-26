#!/usr/bin/env python3
import datetime
z = input("What is the date today in YYYY-MM-dd Format ?")
year, month, day = map(int,z.split('-'))
x = datetime.datetime(year, month, day)
print(x.strftime("%b %d %Y"))

   

        