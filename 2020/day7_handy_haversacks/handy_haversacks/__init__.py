from functools import reduce
from re import search


def color_reducer(color):
    def reducer(a, x):
        if color in x[1]:
            a.append(x[0])
        return a
    return reducer


def count_total_bags(data, color):
    data_with_counts = dict(map(lambda x: parse_rule(x, True), data))
    contents = dict(data_with_counts[color])
    if len(contents) > 0:
        total = 0
        for child in contents.items():
            total += child[1] + child[1] * count_total_bags(data, child[0])
        return total
    else:
        return 0


def count_total_one(data, color):
    total = reduce(lambda a, x: a+x[1], data[color], 0)
    return total


def count_possibilities(data, color):
    return len(collect_possibilities(data, color))


def collect_possibilities(data, color):
    tree = list(map(lambda x: parse_rule(x), data))
    leaves = reduce(color_reducer(color), tree, [])
    final = leaves.copy()
    if len(leaves) > 0:
        for color in leaves:
            parent = collect_possibilities(data, color)
            final.extend(parent)
    else:
        final = []
    res = []
    # remove dups
    [res.append(x) for x in final if x not in res]
    return res


def parse_rule(rule, with_count=False):
    # parse
    result = search(r'^(.+?) (bags contain )(.+)\.$', rule)
    # break contents up into list
    contents = result.groups()[2].split(', ')
    if len(contents) > 0 and contents[0] == 'no other bags':
        contents = []
    else:
        # turn contents into tuple (color, count)
        contents = list(map(lambda x: tuple(reversed(search(r'^(\d+) (.+) bags?$', x).groups())), contents))
        if with_count:
            # turn count into int
            contents = list(map(lambda x: (x[0], int(x[1])), contents))
        else:
            contents = list(map(lambda x: x[0], contents))
    return (result.groups()[0], contents)
