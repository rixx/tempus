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



if __name__ == "__main__":

    if len(sys.argv) == 2:

        if "start" == sys.argv[1]:
            start()


        if ("stop" == sys.argv[1]) or ("pause" == sys.argv[1]):
            stop()

        if "status" == sys.argv[1]:
            status()
