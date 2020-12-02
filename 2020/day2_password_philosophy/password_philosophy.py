#!/usr/bin/env python

import sys
from password_philosophy import \
        count_valid_passwords, \
        password_is_valid, \
        real_toboggan_password_is_valid

if __name__ == '__main__':
    data = []
    for line in sys.stdin:
        if 'Exit' == line.rstrip():
            break
        data.append(line.rstrip())
    print('part 1')
    print(count_valid_passwords(data, password_is_valid))
    print('part 2')
    print(count_valid_passwords(data, real_toboggan_password_is_valid))
