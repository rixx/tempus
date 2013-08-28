#!/usr/bin/env python

import os
import sys
import logging
from lib import input_parser


logfile_path = os.path.expanduser('~') + '/.tempus/log'
logging.basicConfig(filename=logfile_path, level=logging.DEBUG, format="%(asctime)s - %(levelname)s: %(message)s")
logger = logging.getLogger("tempus")

if __name__ == "__main__":

    # if tempus is called with no parameter, print usage directly
    if 1 == len(sys.argv):
        input_parser.print_usage()
        sys.exit(0)

    # otherwise try to call the appropriate function. Failing
    else:
        try:
            input_parser.sys.argv[1](sys.argv[2:])
        except:
            input_parser.print_usage()
            sys.exit(-1)
