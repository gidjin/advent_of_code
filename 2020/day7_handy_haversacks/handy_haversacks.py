#!/usr/bin/env python

import sys
from handy_haversacks import count_possibilities, count_total_bags

if __name__ == '__main__':
    data = []
    for line in sys.stdin:
        if 'Exit' == line.rstrip():
            break
        data.append(line.rstrip())
    print('part 1')
    print(count_possibilities(data, 'shiny gold'))
    print('part 1')
    print(count_total_bags(data, 'shiny gold'))
