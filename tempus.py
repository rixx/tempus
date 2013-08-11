#!/usr/bin/env python

import os
import sys
import math
import time
import csv

logfile_path = os.path.expanduser('~') + '/.tempus/log'

def start():
    writelog(1)

def stop():
    writelog(0)

def writelog(status):
    logfile = open(logfile_path, 'a+')
    logwriter = csv.writer(logfile)

    logwriter.writerow([status, math.trunc(time.time())])

    logfile.close()

def clear():
    try:
        os.remove(logfile_path)
        print("Log has been cleared.")
    except FileNotFoundError:
        print("No logfile at "+logfile_path);

def status():
    
    try:
        logfile = open(logfile_path, 'r')
        logreader = csv.reader(logfile)

    except FileNotFoundError:
        print("You haven't even started yet, or the logfile at "+logfile_path+" has gone missing.");
        return;

    sum_seconds = 0
    status = 0
    lasttimestamp = 0

    for entry in logreader:
        
        entry = [int(i) for i in entry]
        if entry[0] == 1:
            
            if status == 0:
                status = 1
                lasttimestamp = entry[1]

        if entry[0] == 0:

            if status == 1:
                status = 0
                sum_seconds += entry[1] - lasttimestamp


    if (status == 1):
        sum_seconds += math.trunc(time.time()) - lasttimestamp

    print("You have worked "+ str(math.trunc(sum_seconds/60)) +" minutes today.")

    if (status == 1):
        print("Also, you should be working right now!")




if __name__ == "__main__":

    if len(sys.argv) == 2:

        if "start" == sys.argv[1]:
            start()


        if ("stop" == sys.argv[1]) or ("pause" == sys.argv[1]):
            stop()

        if "status" == sys.argv[1]:
            status()

        if "clear" == sys.argv[1]:
            clear()
