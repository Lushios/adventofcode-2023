from itertools import combinations
from math import floor, ceil

with open("input.txt") as file:
    data = file.read().splitlines()


def parse_input(input):
    result = []
    single_group = []
    for line in input:
        if line == '':
            result.append(single_group)
            single_group = []
        else:
            single_group.append(line)
    result.append(single_group)
    return result


def check_if_lines_are_one_off(line1, line2):
    mismatch = False
    for i in range(len(line1)):
        if line1[i] != line2[i]:
            if mismatch:
                return False
            mismatch = True
    return mismatch


def check_for_horizontal_symmetry(group, top_side, bottom_side, row_pair_to_ignore=None):
    for i in range(min((len(group) - bottom_side), top_side + 1)):
        if (top_side - i, bottom_side + i) == row_pair_to_ignore:
            continue
        if group[top_side - i] != group[bottom_side + i]:
            return False
    return True


def check_for_vertical_symmetry(group, left_side, right_side, column_pair_to_ignore=None):
    for i in range(min((len(group[0]) - right_side), left_side + 1)):
        if (left_side - i, right_side + i) == column_pair_to_ignore:
            continue
        if [line[left_side - i] for line in group] != [line[right_side + i] for line in group]:
            return False
    return True


def process_group(group):
    #  look for horizontal symmetry
    for index1, index2 in combinations(range(len(group)), 2):
        if abs(index2 - index1) % 2 == 0:
            continue
        if check_if_lines_are_one_off(group[index1], group[index2]):
            top_edge, bottom_edge = (
                min(index1, index2) + floor(abs(index2 - index1) / 2),
                min(index1, index2) + ceil(abs(index2 - index1) / 2)
            )
            is_symmetrical = check_for_horizontal_symmetry(group, top_edge, bottom_edge, (min(index1, index2), max(index1, index2)))
            if is_symmetrical:
                print(bottom_edge * 100)
                return bottom_edge * 100

    #  look for vertical symmetry
    for index1, index2 in combinations(range(len(group[0])), 2):
        if abs(index2 - index1) % 2 == 0:
            continue
        if check_if_lines_are_one_off([line[index1] for line in group], [line[index2] for line in group]):
            left_edge, right_edge = (
                min(index1, index2) + floor(abs(index2 - index1) / 2),
                min(index1, index2) + ceil(abs(index2 - index1) / 2)
            )
            is_symmetrical = check_for_vertical_symmetry(group, left_edge, right_edge, (min(index1, index2), max(index1, index2)))
            if is_symmetrical:
                print(right_edge)
                return right_edge


groups = parse_input(data)
answer = 0
for group in groups:
    answer += process_group(group)
print(answer)
