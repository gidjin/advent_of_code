from functools import reduce
from re import search
from enum import Enum


def find_repeat_instruction(data, self_correction=False, index=0, accumulator=0, seen=[]):
    if index < len(data):
        if index not in seen:
            seen.append(index)
            current_line = data[index]
            command = parse_command(current_line)
            argument = parse_argument(current_line)
            next_index = index+1
            next_accumulator = accumulator
            if command == Ops.NOP:
                # nothing
                pass
            elif command == Ops.ACC:
                next_accumulator = accumulator+argument
            elif command == Ops.JMP:
                next_index = index+argument
            return find_repeat_instruction(data, self_correction, next_index, next_accumulator, seen)
        elif self_correction:
            return False
    return accumulator


def fix_repeat_instruction(data):
    index = 0
    options = []
    for line in data:
        arg = parse_argument(line)
        if parse_command(line) == Ops.NOP:
            options.append((index, Ops.JMP, arg))
        elif parse_command(line) == Ops.JMP:
            options.append((index, Ops.NOP, arg))
        index += 1

    for option in options:
        copy = data.copy()
        copy[option[0]] = f'{option[1].value} {option[2]}'
        result = find_repeat_instruction(copy, True, 0, 0, [])
        if result is not False:
            return result


def parse_command(line):
    result = search(r'^(\w+) .*$', line)
    command = result.groups()[0]
    return Ops(command)


def parse_argument(line):
    result = search(r'^.*? (.+)', line)
    operator = int(result.groups()[0])
    return operator


class Ops(Enum):
    NOP = "nop"
    ACC = "acc"
    JMP = "jmp"
