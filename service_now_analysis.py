#!/usr/bin/python
import datetime as dt
import sys
import re

def parse_time(date):

    date = date.split(" ")
    date = date[0]
    date = date.split("-")
    date = dt.date(int(date[0]),int(date[1]),int(date[2]))
    return date

def main():

    files = open("/home/alex/Downloads/incident.csv", 'r')
    for line in sys.stdin:
        line = line.rstrip("\n")
        line = line.split('","')
        open_date = line[7]
        close_date = line[11]
        ci = line[8]
        if open_date:
            open_date = parse_time(open_date)
        if close_date:
            close_date = parse_time(close_date)
        time_worked = close_date - open_date
        print ci + "|" + str(time_worked)

if __name__=="__main__":
    sys.exit(main())
