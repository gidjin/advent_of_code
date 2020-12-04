from functools import reduce
from re import search
from enum import Enum


def count_valid(data, strict=False):
    passports = parse_multiple(data)
    if strict:
        return reduce(is_valid_strict_reducer, passports, 0)
    else:
        return reduce(is_valid_reducer, passports, 0)


def is_valid_reducer(acc, passport):
    if is_valid_passport(passport):
        acc = acc + 1
    return acc


def is_valid_strict_reducer(acc, passport):
    if is_valid_passport(passport, True):
        acc = acc + 1
    return acc

def is_valid_passport(passport, strict=False):
    required_fields = filter(lambda f: f != PassportFields.COUNTRY_ID, list(PassportFields))
    return reduce(lambda a, f: a and f in passport.keys(), required_fields, True) and \
            (strict is False or check_criteria(passport))


def check_criteria(passport):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if (int(passport.get(PassportFields.BIRTH_YEAR)) < 1920 or
            int(passport.get(PassportFields.BIRTH_YEAR)) > 2002):
        return False
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    if (int(passport.get(PassportFields.ISSUE_YEAR)) < 2010 or
            int(passport.get(PassportFields.ISSUE_YEAR)) > 2020):
        return False
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    if (int(passport.get(PassportFields.EXPIRATION_YEAR)) < 2020 or
            int(passport.get(PassportFields.EXPIRATION_YEAR)) > 2030):
        return False
    # hgt (Height) - a number followed by either cm or in:
    result = search(r'^(\d+)(\w\w)$', passport.get(PassportFields.HEIGHT))
    if result is None:
        return False
    matches = result.groups()
    #  If cm, the number must be at least 150 and at most 193.
    if matches[1] == "cm" and (int(matches[0]) < 150 or int(matches[0]) > 193):
        return False
    #  If in, the number must be at least 59 and at most 76.
    if matches[1] == "in" and (int(matches[0]) < 59 or int(matches[0]) > 76):
        return False
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    result = search(r'^#[0-9a-fA-F]{6}$', passport.get(PassportFields.HAIR_COLOR))
    if result is None:
        return False
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    result = search(r'^(amb|blu|brn|gry|grn|hzl|oth)$', passport.get(PassportFields.EYE_COLOR))
    if result is None:
        return False
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    result = search(r'^\d{9}$', passport.get(PassportFields.PASSPORT_ID))
    if result is None:
        return False
    return True


def multi_reducer(acc, line):
    last_idx = len(acc)-1
    if line != "":
        if len(acc[last_idx]) > 0:
            acc[last_idx] = acc[last_idx] + " " + line
        else:
            acc[last_idx] = line
    else:
        acc.append("")
    return acc


def parse_multiple(lines):
    reduced = reduce(multi_reducer, lines, [""])
    filtered = filter(lambda i: i != "", reduced)
    return list(map(parse_passport, filtered))


def parse_passport_field(field):
    result = search(r'^([^:]+):([^:]+)$', field)
    if result is not None:
        matches = result.groups()
        return (PassportFields(matches[0]), matches[1])


def parse_passport(string):
    nonewline = string.replace("\n", " ").replace("\r", "")
    split_fields = nonewline.split(" ")
    fields = map(parse_passport_field, split_fields)
    dict_fields = dict(fields)
    return dict_fields


class PassportFields(Enum):
    BIRTH_YEAR = "byr"
    COUNTRY_ID = "cid"
    EXPIRATION_YEAR = "eyr"
    EYE_COLOR = "ecl"
    HAIR_COLOR = "hcl"
    HEIGHT = "hgt"
    ISSUE_YEAR = "iyr"
    PASSPORT_ID = "pid"
