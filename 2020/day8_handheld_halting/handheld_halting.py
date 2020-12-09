#!/usr/bin/env python

import sys
from handheld_halting import find_repeat_instruction, fix_repeat_instruction

if __name__ == '__main__':
    data = []
    for line in sys.stdin:
        if 'Exit' == line.rstrip():
            break
        data.append(line.rstrip())
    print('part 1')
    print(find_repeat_instruction(data))
    print('part 2')
    print(fix_repeat_instruction(data))
