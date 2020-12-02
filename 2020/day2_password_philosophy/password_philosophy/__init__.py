from functools import reduce
from re import search, findall


def parse_password_data(data):
    result = search(r'^(\d+)-(\d+) (\w): (\w+)$', data)
    if result is not None:
        matches = result.groups()
        return (int(matches[0]), int(matches[1]), matches[2], matches[3])


def password_is_valid(data):
    (min_count, max_count, letter, password) = data
    result = findall(rf'{letter}', password)
    if result is not None:
        if min_count <= len(result) and max_count >= len(result):
            return True
    return False


def real_toboggan_password_is_valid(data):
    # correct for 1 index position in password policy
    (pos1, pos2, letter, password) = data
    if password[pos1-1] == letter and password[pos2-1] != letter:
        return True
    elif password[pos1-1] != letter and password[pos2-1] == letter:
        return True
    return False


def count_valid_passwords(passwords_and_data, check_valid):
    mapped = map(lambda x: parse_password_data(x), passwords_and_data)
    return reduce(lambda a, x: a + 1 if check_valid(x) else a, mapped, 0)
