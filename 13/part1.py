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


def check_for_horizontal_symmetry(group, top_side, bottom_side):
    for i in range(1, min((len(group) - bottom_side), top_side + 1)):
        if group[top_side - i] != group[bottom_side + i]:
            return False
    return True


def check_for_vertical_symmetry(group, left_side, right_side):
    for i in range(1, min((len(group[0]) - right_side), left_side + 1)):
        if [line[left_side - i] for line in group] != [line[right_side + i] for line in group]:
            return False
    return True


def process_group(group):
    #  look for horizontal symmetry
    for i in range(1, len(group)):
        if group[i - 1] == group[i]:
            is_symmetrical = check_for_horizontal_symmetry(group, i-1, i)
            if is_symmetrical:
                print(i * 100)
                return i * 100
    # look for vertical symmetry
    for i in range(1, len(group[0])):
        if [line[i - 1] for line in group] == [line[i] for line in group]:
            is_symmetrical = check_for_vertical_symmetry(group, i - 1, i)
            if is_symmetrical:
                print(i)
                return i


groups = parse_input(data)
answer = 0
for group in groups:
    answer += process_group(group)
print(answer)
