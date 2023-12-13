from re import finditer
from itertools import chain, combinations

with open("input.txt") as file:
    data = file.read().splitlines()


def powerset(iterable):
    """This is from itertools docs, and I'm not gonna pretend it is not"""
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def parse_line(line):
    springs, damaged_groups_str = line.split(' ')
    damaged_groups = [int(group) for group in damaged_groups_str.split(',')]
    return springs, damaged_groups


def springs_options(springs: str ):
    matches = [match.start() for match in finditer(r'\?', springs)]
    matches_powerset = powerset(matches)
    for matches_combination in matches_powerset:
        new_springs = list(springs)
        for match in matches_combination:
            new_springs[match] = '#'
        yield ''.join(new_springs).replace('?', '.')


def springs_option_valid(springs, damaged_groups):
    matches = finditer('#+', springs)
    match_lengths = [match.end() - match.start() for match in matches]
    return match_lengths == damaged_groups


def get_line_options(springs, damaged_groups):
    spring_options = 0
    for option in springs_options(springs):
        if springs_option_valid(option, damaged_groups):
            spring_options += 1
    return spring_options


result = 0
for line_number, line in enumerate(data):
    springs, damaged_groups = parse_line(line)
    result += get_line_options(springs, damaged_groups)
print(result)


