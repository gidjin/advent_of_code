from itertools import permutations
from functools import reduce


def reducer(result, items):
    if result is None:
        total = reduce(lambda s, x: s+x, items)
        if total == 2020:
            return items
    return result


def find_pair_2020(data):
    perms = permutations(data, 2)
    return reduce(reducer, list(perms), None)


def calculate_answer(data):
    pair = find_pair_2020(data)

    return reduce(lambda m, x: m*x, pair)


def find_triple_2020(data):
    perms = permutations(data, 3)
    return reduce(reducer, list(perms), None)


def calculate_answer_two(data):
    pair = find_triple_2020(data)

    return reduce(lambda m, x: m*x, pair)
