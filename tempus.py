#!/usr/bin/env python

import os
import sys
import logging
from lib.input_parser import *


logfile_path = os.path.expanduser('~') + '/.tempus/log'
logging.basicConfig(filename=logfile_path, level=logging.DEBUG, format="%(asctime)s - %(levelname)s: %(message)s")
logger = logging.getLogger("tempus")

input_mapper = dict(start=start, pause=pause, stop=stop, add=add, list=list, tag=tag, untag=untag, rename=rename,
                    status=status, clear=clear, remove=remove)

if __name__ == "__main__":

    # if tempus is called with no parameter, print usage directly
    if 1 == len(sys.argv):
        print_usage()
        sys.exit(0)

    # otherwise try to call the appropriate function. Failing
    else:
        #try:
            logger.debug("Invoking " + sys.argv[1] + ".")
            return_code = input_mapper[sys.argv[1]](sys.argv[2:])
            logger.debug("Finished with return code " + str(return_code))

            if return_code:
                sys.exit(0)
            else:
                sys.exit(-1)

        #except KeyError:
        #    logger.debug("Error invoking " + sys.argv[1] + ".")
        #    print_usage()
        #    sys.exit(-1)
