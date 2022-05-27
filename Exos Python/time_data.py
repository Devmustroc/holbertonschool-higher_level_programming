#!/usr/bin/python3
"""Write a python programm to display the current time.
"""
import datetime
now = datetime.datetime.now()
print("Current date and time: ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))
