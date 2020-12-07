#!/usr/bin/env python

import sys
from custom_customs import calculate_total, calculate_total_part2

if __name__ == '__main__':
    data = []
    for line in sys.stdin:
        if 'Exit' == line.rstrip():
            break
        data.append(line.rstrip())
    print('part 1')
    print(calculate_total(data))
    print('part 2')
    print(calculate_total_part2(data))
