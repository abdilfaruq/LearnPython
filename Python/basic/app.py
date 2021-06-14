#Module

"""
import data as d

print(d.person)
print(d.printNama("jack"))

from data import person, printNama

print(person)
print(printNama("jack"))
"""

import data

print(data.person)
print(data.printNama("jack"))

#Built in Module
"""
import datetime

date = datetime.datetime(2021, 1, 13)
print(date)
"""
import datetime

now = datetime.datetime.now()
print("\n",now)
print(now.strftime("%Y, %B, %d"))