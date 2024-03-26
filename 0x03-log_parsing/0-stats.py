#!/usr/bin/python3
import sys

status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) > 2:
            status = parts[-2]
            size = parts[-1]

            if status.isdigit():
                status = int(status)
                if status in status_codes:
                    status_codes[status] += 1

            if size.isdigit():
                total_size += int(size)

            line_count += 1

            if line_count % 10 == 0:
                print("File size: {}".format(total_size))
                for code, count in sorted(status_codes.items()):
                    if count:
                        print("{}: {}".format(code, count))

except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        if count:
            print("{}: {}".format(code, count))
