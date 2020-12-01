#!/usr/bin/env python

import sys
from report_repair import calculate_answer, calculate_answer_two

if __name__ == '__main__':
    data = []
    for line in sys.stdin:
        if 'Exit' == line.rstrip():
            break
        data.append(int(line.rstrip()))
    print('part 1')
    print(calculate_answer(data))
    print('part 2')
    print(calculate_answer_two(data))
