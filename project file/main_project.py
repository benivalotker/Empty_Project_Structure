# Title
# Version - 1.0
# Update Date - 01-07-20 00:00
# Update Description - First update. 
# Description - Descriptions about the service.
# ------------------------------------------------------------------------
import json
import config
import traceback
from logging_pkg import log_rotating 

def main():
    try:
        logs = log_rotating.init_log("log_name")
    except Exception as ex:
        # handle exception
        print(traceback.format_exc())


if __name__ == "__main__":
    main()