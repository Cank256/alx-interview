#!/usr/bin/python3
"""
This module contains a function that validates UTF-8 encoding
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding

    Args:
        data (list(int)): A list of integers representing 1 byte of data each

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False
    """
    if data is None or len(data) == 0:
        return False

    num_bytes = 0
    for byte in data:
        if num_bytes == 0:
            if byte >> 5 == 0b110:
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                num_bytes = 3
            elif byte >> 7 == 0b1:
                return False
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0