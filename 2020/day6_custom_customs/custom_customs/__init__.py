from functools import reduce
from itertools import chain


def unique_group_list(group):
    segments = map(lambda a: [char for char in a], group)
    flat_list = list(chain.from_iterable(segments))
    flat_list = list(filter(lambda i: i != ' ', flat_list))
    res = []
    # remove dups
    [res.append(x) for x in flat_list if x not in res]
    return list(res)


def shared_answer_list(group):
    segments = list(map(lambda a: [char for char in a], group))
    group_size = reduce(lambda a, i: a+1 if i[0] == ' ' else a, segments, 1)
    flat_list = list(chain.from_iterable(segments))
    flat_list = list(filter(lambda i: i != ' ', flat_list))
    uniq = []
    # remove dups
    [uniq.append(x) for x in flat_list if x not in uniq]
    counts = dict(map(lambda a: (a, 0), uniq))
    for char in flat_list:
        counts[char] += 1
    final = list(dict(filter(lambda i: i[1] == group_size, counts.items())))
    return final


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


def parse_groups(lines):
    reduced = reduce(multi_reducer, lines, [""])
    filtered = filter(lambda i: i != "", reduced)
    return list(filtered)


def calculate_total(lines):
    groups = list(map(lambda i: i.replace(" ", ""), parse_groups(lines)))
    total = reduce(lambda a, i: a + len(unique_group_list(i)), groups, 0)
    return total


def calculate_total_part2(lines):
    groups = parse_groups(lines)
    total = reduce(lambda a, i: a + len(shared_answer_list(i)), groups, 0)
    return total
