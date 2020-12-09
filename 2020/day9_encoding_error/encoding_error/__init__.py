from itertools import permutations
from functools import reduce


def is_valid(preamble, number):
    perms = list(permutations(preamble, 2))
    return reduce(lambda a, x: a or x[0] + x[1] == number and x[0] != x[1], perms, False)


def find_list_adding_to(data, number, start=0):
    num_data = list(map(lambda x: int(x), data))[start:]
    end = start+1
    total = num_data[start]
    while end < len(num_data) and total < number:
        total += num_data[end]
        end += 1
    if total > number and end < len(num_data):
        return find_list_adding_to(data, number, start+1)
    else:
        return num_data[start:end]


def find_first_invalid(data, preamble_size=25):
    num_data = list(map(lambda x: int(x), data))
    index = 0
    while index < len(num_data):
        end = index+preamble_size
        if is_valid(num_data[index:end], num_data[end]):
            pass
        else:
            return num_data[end]
        index += 1


def encryption_weakness(data, number):
    nums = find_list_adding_to(data, number)
    nums.sort()
    return nums[0] + nums[len(nums)-1]
