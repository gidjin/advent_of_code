from functools import reduce
from re import search, findall
from enum import Enum


def is_tree(square):
    if Space(square) == Space.TREE:
        return True
    return False


def count_trees(data, right, down):
    i = 0
    j = 0
    total = 0
    while i < len(data):
        if j >= len(data[i]):
            j = j - len(data[i])
        if is_tree(data[i][j]):
            total = total + 1
        i = i + down
        j = j + right

    return total


def count_right3_down1_trees(data):
    return count_trees(data, 3, 1)


def multiply_all(tree_counts):
    return reduce(lambda a, x: a*x, tree_counts, 1)


class Space(Enum):
    OPEN = '.'
    TREE = '#'
