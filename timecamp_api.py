#!/usr/bin/python
import sys
import re
import requests
import json
import datetime
###########
# Examples#
# curl "https://www.timecamp.com/third_party/api/tasks/format/json/api_token/b5eb748ef107f69d9ff76d5671/from/2018-06-24/to/2018-06-30/user_ids/17591"
# curl "https://www.timecamp.com/third_party/api/entries/format/json/api_token/abca7d132c1be87729b7c6239e/from/2018-06-24/to/2018-06-30/user_ids/1091853"

def parse_json(json_string):

    delim = "|"
    report = []
    parsed_json = json.loads(json_string)
    report.append("User Name" + delim + "Task Name" + delim + "Start Time" + delim + "End Time" + delim + "Duration")
    for line in parsed_json:
#        print line
        user_name = line['user_name']
        start = line['start_time']
        end = line['end_time']
        name = line['name']
        duration = datetime.datetime.strptime(end, "%H:%M:%S") - datetime.datetime.strptime(start, "%H:%M:%S")
        duration = duration / 60
        duration = str(duration)
        report.append(user_name + delim + name + delim + start + delim + end + delim + duration)
    return report

def main():

    url = "https://www.timecamp.com/third_party/api/entries/format/json/api_token/{apikey}/from/{start_date}/to/{end_date}/user_ids/{user_ids}"
    ###########################
    # Read configuration file #
    ###########################
    config = open("/home/alex/bincustom/files/timecamp_apis.cfg", "r")
    pat = re.compile("(.*?)=(.*)")
    for line in config:
        line = line.rstrip("\n")
        m = pat.match(line)
        if m:
            if m.group(1) == "lisa_id":
                lisa_id = m.group(2)
            if m.group(1) == "lisa_api":
                lisa_api = m.group(2)
            if m.group(1) == "alex_id":
                alex_id = m.group(2)
            if m.group(1) == "alex_api":
                alex_api = m.group(2)
    ###########################
    # Set start and end dates #
    ###########################
    now = datetime.datetime.now()
    start_delta = datetime.timedelta(days=8)
    start_date = now - start_delta
    start_date = start_date.strftime("%Y-%m-%d")
    end_delta = datetime.timedelta(days=2)
    end_date = now - end_delta
    end_date = end_date.strftime("%Y-%m-%d")
    #################
    # Make API call #
    #################
    url = url.replace("{apikey}", lisa_api)
    url = url.replace("{user_ids}", lisa_id)
    url = url.replace("{start_date}", str(start_date))
    url = url.replace("{end_date}", str(end_date))
    r = requests.get(url)
    ##############
    # Parse JSON #
    ##############
    result = parse_json(r.text)
    for line in result:
        print line

if __name__=="__main__":
    sys.exit(main())
