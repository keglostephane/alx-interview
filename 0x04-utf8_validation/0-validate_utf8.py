#!/usr/bin/python3
"""UTF_8_validation

UTF-8 code units (characters, glyph) are encoded with a max of 4 bytes.
the leftmost bits in the start byte indicate the number of bytes
used to encode the character or glyph as following:
01XXXXXX : 1 byte character
11XXXXXX : 2 bytes character
111XXXXX : 3 bytes character
1111XXXX: 4 bytes character
the remaining bytes called continuation bytes : 10XXXXXX
are used to encode the character.
"""


def validUTF8(data):
    """Check if a data set is a valid UTF-8 encoding"""
    bytes_num = 0   # number of bytes in data
    mask = 1 << 7

    for num in data:
        bits = num & 0xFF   # keep only significant 8 digits
        # check for a new UTF-8 code unit
        if bytes_num == 0:
            # calculate the number of leading 1 in the byte
            while bits & mask:
                bytes_num += 1
                mask >>= 1
            # detect a ASCII character
            if bytes_num == 0:
                continue
            if bytes_num == 1 and num >> 6 == 0b10:
                continue
            if bytes_num > 4:
                return False
        else:
            if num >> 6 != 0b10:
                return False
        # the number of continuation bytes remaining in a detected code unit
        bytes_num -= 1

    return bytes_num == 0
