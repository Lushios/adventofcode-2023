from re import finditer
from itertools import chain, combinations

with open("input.txt") as file:
    data = file.read().splitlines()


def powerset(iterable, length_limit):
    """This is from itertools docs, and I'm not gonna pretend it is not"""
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    print(length_limit)
    return chain.from_iterable(combinations(s, r) for r in range(length_limit + 1))


def parse_line(line):
    springs, damaged_groups_str = line.split(' ')
    final_springs = '?'.join([springs for _ in range(5)])
    damaged_groups = ','.join([damaged_groups_str for _ in range(5)])
    final_groups = [int(group) for group in damaged_groups.split(',')]
    return final_springs, final_groups


def springs_options(springs: str, damaged_groups):
    matches = [match.start() for match in finditer(r'\?', springs)]
    matches_powerset = powerset(matches, sum(damaged_groups) - springs.count('#'))
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
    for option in springs_options(springs, damaged_groups):
        if springs_option_valid(option, damaged_groups):
            spring_options += 1
    return spring_options


result = 0
for line_number, line in enumerate(data):
    print(line_number)
    springs, damaged_groups = parse_line(line)
    print(springs, damaged_groups)
    result += get_line_options(springs, damaged_groups)
print(result)


