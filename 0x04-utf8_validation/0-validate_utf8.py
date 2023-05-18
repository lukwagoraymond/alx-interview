#!/usr/bin/python3
"""
Module containing function that validates
if integer in list is a valid UTF-8 encoding
"""


def validUTF8(data):
    """UTF-8 Validator Method returns
    True or False"""
    leading_onez_count = 0
    for number in data:
        bit = 0b10000000
        if not leading_onez_count:
            while bit & number:
                leading_onez_count += 1
                bit >>= 1
            if leading_onez_count > 4:
                return False
            elif leading_onez_count:
                leading_onez_count -= 1
                if leading_onez_count == 0:
                    return False
        elif leading_onez_count > 0:
            if number >> 6 != 2:
                return False
            leading_onez_count -= 1
    return not leading_onez_count

    """index = 0
    encoded_data = iter(data)
    for index in encoded_data:
        leading_ones = count_significant_ones(index)

        if leading_ones in [1, 7, 8]:
            return False

        for _ in range(leading_ones - 1):
            significant_byte = next(encoded_data, None)
            if significant_byte is None or significant_byte >> 6 != 0b10:
                return False
    return True"""


"""def count_significant_ones(byte):
    \"""Counts the leading one bytes.\"""
    count = 0
    mask = 0b10000000

    while byte & mask:
        count += 1
        mask >>= 1

    return count"""
