#!/usr/bin/env python

import sys
from toboggan_trajectory import \
        count_right3_down1_trees, count_trees, multiply_all

if __name__ == '__main__':
    data = []
    for line in sys.stdin:
        if 'Exit' == line.rstrip():
            break
        data.append(line.rstrip())
    print('part 1')
    print(count_right3_down1_trees(data))
    print('part 2')
    result = [
            count_trees(data, 1, 1),
            count_trees(data, 3, 1),
            count_trees(data, 5, 1),
            count_trees(data, 7, 1),
            count_trees(data, 1, 2)
            ]
    print(result)
    print(multiply_all(result))
