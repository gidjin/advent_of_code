#!/usr/bin/env python

import sys
from passport_processing import count_valid

if __name__ == '__main__':
    data = []
    for line in sys.stdin:
        if 'Exit' == line.rstrip():
            break
        data.append(line.rstrip())
    print('part 1')
    print(count_valid(data))
    print('part 2')
    print(count_valid(data, True))
