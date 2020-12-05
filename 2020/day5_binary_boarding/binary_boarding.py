#!/usr/bin/env python

import sys
from binary_boarding import find_highest_seat, find_missing_seat, get_all_seat_ids

if __name__ == '__main__':
    data = []
    for line in sys.stdin:
        if 'Exit' == line.rstrip():
            break
        data.append(line.rstrip())
    print('part 1')
    print(find_highest_seat(data))
    print('part 2')
    print(find_missing_seat(get_all_seat_ids(data)))
