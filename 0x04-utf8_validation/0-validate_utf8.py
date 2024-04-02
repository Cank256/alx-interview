#!/usr/bin/python3
def validUTF8(data):
    # Function to check if a byte is a start of a UTF-8 sequence
    def is_start_of_utf8(byte):
        return byte >> 7 == 0b0 or (byte >> 5) == 0b110 \
            or (byte >> 4) == 0b1110 or (byte >> 3) == 0b11110

    # Function to check if a byte is a continuation byte
    def is_continuation_byte(byte):
        return (byte >> 6) == 0b10

    # Loop through each byte in the data
    i = 0
    while i < len(data):
        byte = data[i]
        if is_start_of_utf8(byte):
            # Determine the number of bytes in the sequence
            if byte >> 7 == 0b0:  # 1-byte character
                length = 1
            elif (byte >> 5) == 0b110:  # 2-byte character
                length = 2
            elif (byte >> 4) == 0b1110:  # 3-byte character
                length = 3
            elif (byte >> 3) == 0b11110:  # 4-byte character
                length = 4
            else:
                return False  # Invalid start byte
            # Check the following bytes in the sequence
            for j in range(1, length):
                if i + j >= len(data) or not is_continuation_byte(data[i + j]):
                    return False
            # Move to the next byte after the sequence
            i += length
        else:
            return False  # Invalid start of UTF-8 sequence
    return True
