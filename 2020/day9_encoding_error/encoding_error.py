#!/usr/bin/env python

import sys
from encoding_error import find_first_invalid, encryption_weakness

if __name__ == '__main__':
    data = []
    for line in sys.stdin:
        if 'Exit' == line.rstrip():
            break
        data.append(line.rstrip())
    print('part 1')
    invalid_number = find_first_invalid(data)
    print(invalid_number)
    print('part 2')
    print(encryption_weakness(data, invalid_number))
