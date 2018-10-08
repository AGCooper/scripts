#!/usr/bin/python3
import datetime as dt
import time
import os
import sys

def do_something(start_time):

    current_time = dt.datetime.now()
    duration = current_time - start_time
    time.sleep(1)
    return duration

def main():

    count = 10
    start_time_c = time.ctime()
    start_time = dt.datetime.now()
    while count > 0:
        result = do_something(start_time)
        print(result)
        count -= 1
    end_time_c = time.ctime()
    print("This process began at: " + start_time_c + "\n" + "This process ended at: " + end_time_c + "\n")

if __name__=="__main__":
   sys.exit(main())
