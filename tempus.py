#!/usr/bin/env python

import os
import sys
import math
import time
import csv
import logging

timefile_path = os.path.expanduser('~') + '/.tempus/time'
logfile_path = os.path.expanduser('~') + '/.tempus/log'

def start():
    writelog(1)

def stop():
    writelog(0)

def writelog(status):
    logfile = open(timefile_path, 'a+')
    logwriter = csv.writer(logfile)

    logwriter.writerow([status, math.trunc(time.time())])
    logger.debug("Wrote "+str(status)+" to "+timefile_path+".")

    logfile.close()

def clear():
    try:
        os.remove(timefile_path)
        print("Log has been cleared.")
        logger.info("Log has been cleared")
    except FileNotFoundError:
        print("No file at "+timefile_path);
        logger.info("No file at "+timefile_path+".")

def status():
    
    try:
        logfile = open(logfile_path, 'r')
        logreader = csv.reader(logfile)

    except FileNotFoundError:
        print("You haven't even started yet, or the file at "+timefile_path+" has gone missing.");
        logger.error("File at "+timefile_path+" does not exist.")
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
    logger.info("Printed status.")


logging.basicConfig(filename=logfile_path, level=logging.DEBUG, format="%(asctime)s - %(levelname)s: %(message)s")
logger = logging.getLogger("tempus")

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
