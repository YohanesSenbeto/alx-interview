#!/usr/bin/python3


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data: A list of integers representing bytes of data.

    Returns:
        True if data is a valid UTF-8 encoding, else False.
    """

    """function to check if a byte is a valid start of a UTF-8 character"""

    def is_start_byte(byte):
        return (
            (byte >> 7) == 0b0
            or (byte >> 5) == 0b110
            or (byte >> 4) == 0b1110
            or (byte >> 3) == 0b11110
        )

    """Iterate through the data list"""
    i = 0
    while i < len(data):
        byte = data[i]

        """Check if byte is a valid start of a UTF-8 character"""
        if not is_start_byte(byte):
            return False

        """Determine the number of bytes in the UTF-8 character"""
        if (byte >> 7) == 0b0:
            """Single-byte character"""
            i += 1
        elif (byte >> 5) == 0b110:
            """Two-byte character"""
            if i + 1 >= len(data) or (data[i + 1] >> 6) != 0b10:
                return False
            i += 2
        elif (byte >> 4) == 0b1110:
            """Three-byte character"""
            if (
                i + 2 >= len(data)
                or (data[i + 1] >> 6) != 0b10
                or (data[i + 2] >> 6) != 0b10
            ):
                return False
            i += 3
        elif (byte >> 3) == 0b11110:
            """Four-byte character"""
            if (
                i + 3 >= len(data)
                or (data[i + 1] >> 6) != 0b10
                or (data[i + 2] >> 6) != 0b10
                or (data[i + 3] >> 6) != 0b10
            ):
                return False
            i += 4
        else:
            """Invalid byte"""
            return False

    return True
