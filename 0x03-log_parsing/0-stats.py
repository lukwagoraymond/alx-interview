#!/usr/bin/python3
"""Script that reads stdin line by line and
computes metrics"""

import re
import sys

counter = 0
file_size = 0
status_code_counter = {200: 0, 301: 0, 400: 0, 401: 0,
                       403: 0, 404: 0, 405: 0, 500: 0}


def print_code_count(dic, file_size):
    """Prints out the status code counts"""
    print(f"File size: {file_size}")
    for key in sorted(dic.keys()):
        if dic[key] != 0:
            print(f"{key}: {dic[key]}")


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            split_string = re.split('- |"|"| " " ', str(line))
            status_and_file_s = split_string[-1]
            if counter != 0 and counter % 10 == 0:
                print_code_count(status_code_counter, file_size)
            counter += 1
            try:
                status_code, f_size = map(int, status_and_file_s.split())
                if status_code in status_code_counter:
                    status_code_counter[status_code] += 1
                file_size += f_size
            except ValueError:
                pass
            if counter % 10 == 0:
                print_code_count(status_code_counter, file_size)
        print_code_count(status_code_counter, file_size)
    except KeyboardInterrupt:
        print_code_count(status_code_counter, file_size)
        raise
