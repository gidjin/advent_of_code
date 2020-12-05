from functools import reduce
from re import search


def get_all_seat_ids(boarding_passes):
    return list(map(lambda i: calculate_seat_id(code_to_seat_location(i)), boarding_passes))


def find_missing_seat(seat_ids):
    seat_ids.sort()
    i = 0
    while i < len(seat_ids):
        if i-1 > 0:
            if seat_ids[i-1] + 2 == seat_ids[i]:
                return seat_ids[i-1] + 1
        i = i + 1


def find_highest_seat(boarding_passes):
    all_seat_ids = get_all_seat_ids(boarding_passes)
    highest = reduce(lambda a, i: a if a > i else i, all_seat_ids)
    return highest


def calculate_seat_id(seat):
    return seat[0] * 8 + seat[1]


def code_to_seat_location(code):
    matches = search(r'^((F|B){7})((L|R){3})$', code)
    groups = matches.groups()
    row = find_row(groups[0])
    col = find_col(groups[2])
    return (row, col)


# 0 - 127
def find_row(string, start=0, end=127, total=128):
    if len(string) == 1:
        if string[0] == "F":
            return int(start)
        elif string[0] == "B":
            return int(end)
    elif len(string) > 1:
        if string[0] == "F":
            return find_row(string[1:], start, end - total/2, total/2)
        elif string[0] == "B":
            return find_row(string[1:], start + total/2, end, total/2)


# 0 - 7
def find_col(string, start=0, end=7, total=8):
    if len(string) == 1:
        if string[0] == "L":
            return int(start)
        elif string[0] == "R":
            return int(end)
    elif len(string) > 1:
        if string[0] == "L":
            return find_col(string[1:], start, end - total/2, total/2)
        elif string[0] == "R":
            return find_col(string[1:], start + total/2, end, total/2)
