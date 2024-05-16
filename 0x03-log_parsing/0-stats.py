#!/usr/bin/python3
"""101-stats

Read stdin line by line and compute metric.
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
              <status code> <file size>

Each 10 lines and after a keyboard interruption, prints those statistics:

File size: <total size>
``total size``: the sum of all previous file size

<status code>: <number>
possible ``status code``: 200, 301, 400, 401, 403, 404, 405, 500
``number``: number of line by status code
"""
import sys

tline = 0
size = 0
status_code = ["200", "301", "400", "401", "403", "404", "405", "500"]
status = []

try:
    for line in sys.stdin:
        tline += 1
        data = line.split()
        if len(data) >= 2 and data[-1].isdigit():
            status_value = data[-2]
            filesize = int(data[-1])
            size += filesize
            status.append(status_value)

        if tline == 10:
            tline = 0
            print(f"File size: {size:d}")
            for code in status_code:
                if code in status:
                    print(f"{code}: {status.count(code):d}")
except KeyboardInterrupt:
    pass
finally:
    print(f"File size: {size:d}")
    for code in status_code:
        if code in status:
            print(f"{code}: {status.count(code):d}")
