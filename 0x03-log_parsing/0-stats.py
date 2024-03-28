#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


def print_statistics(total_file_size, status_code_counts):
    """Prints accumulated metrics.

    Args:
        total_file_size (int): Accumulated file size.
        status_code_counts (dict): Count of status codes.
    """
    print("Total file size:", total_file_size)
    for code, count in sorted(status_code_counts.items()):
        print(f"{code}: {count}")


if __name__ == "__main__":
    import sys

    total_file_size = 0
    status_code_counts = {}
    a = '200', '301', '400', '401', '403', '404', '405', '500'
    valid_status_codes = {a}
    lines_processed = 0

    try:
        for line in sys.stdin:
            lines_processed += 1
            if lines_processed % 10 == 0:
                print_statistics(total_file_size, status_code_counts)

            parts = line.split()
            try:
                file_size = int(parts[-1])
                total_file_size += file_size
            except (ValueError, IndexError):
                pass

            try:
                status_code = parts[-2]
                if status_code in valid_status_codes:
                    b = status_code_counts.get(status_code, 0) + 1
                    status_code_counts[status_code] = b
            except IndexError:
                pass

        print_statistics(total_file_size, status_code_counts)

    except KeyboardInterrupt:
        print_statistics(total_file_size, status_code_counts)
        sys.exit(0)
