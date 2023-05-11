#!/usr/bin/python3
"""Script that reads stdin line by line and
computes metrics"""

import re
import sys

counter = 0
file_size = 0
# Store the count of all status_codes in a dictionary
status_code_counter = {200: 0, 301: 0, 400: 0,
                       401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


def printCodeCount(dic, file_siz):
    """Prints out the status code counts"""
    print("File size: {}".format(file_siz))
    for key in sorted(dic.keys()):
        if status_code_counter[key] != 0:
            print("{}: {}".format(key, dic[key]))


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            split_string = re.split('- |"|"| " " ', str(line))
            statusC_and_file_s = split_string[-1]
            if counter != 0 and counter % 10 == 0:
                printCodeCount(status_code_counter, file_size)
            counter = counter + 1
            try:
                statusC = int(statusC_and_file_s.split()[0])
                f_size = int(statusC_and_file_s.split()[1])
                if statusC in status_code_counter:
                    status_code_counter[statusC] += 1
                file_size = file_size + f_size
            except ValueError:
                pass
        printCodeCount(status_code_counter, file_size)
    except KeyboardInterrupt:
        printCodeCount(status_code_counter, file_size)
        raise
