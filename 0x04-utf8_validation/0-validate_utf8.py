#!/usr/bin/python3
"""UTF_8_validation

UTF-8 characters are encoded with a max of 4 bytes.
the leftmost bits in the start byte indicate the number of bytes
used to encode the character as following:
01XXXXXX : 1 byte character
11XXXXXX : 2 bytes characters
111XXXXX : 3 bytes characters
1111XXXX: 4 bytes characters
the remaining bytes called continuation bytes : 10XXXXXX
are used to encode the number.
"""


def validUTF8(data):
    """Check if a data set is a valid UTF-8 encoding"""
    bytes_num = 0   # number of bytes in data
    mask = 1 << 7

    for num in data:
        bits = num & 0xFF   # keep only significant 8 digits

        if bytes_num == 0:
            # calculate the number of leading 1 in the byte
            while bits & mask:
                bytes_num += 1
                mask >>= 1
            if bytes_num == 0:
                continue
            if bytes_num == 1 or bytes_num > 4:
                return False
        else:
            if num >> 6 != 0b10:
                return False
        # the number of continuation bytes remaining in data
        bytes_num -= 1

    return bytes_num == 0
