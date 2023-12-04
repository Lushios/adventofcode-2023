from functools import lru_cache

with open("input.txt") as file:
    data = file.read().splitlines()


def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper


def get_numbers_from_string(string: str):
    return [int(number.strip()) for number in string.split(' ') if number]


@lru_cache
def get_line_children(line_number: int, line: str):
    left_part, right_part = line.split(' | ')
    winning_numbers = get_numbers_from_string(left_part.split(': ')[1])
    actual_numbers = get_numbers_from_string(right_part)
    intersection_count = len([number for number in winning_numbers if number in actual_numbers])
    return [line_number + i for i in range(1, intersection_count + 1)]


@count_calls
def process_line(line_number: int, line: str):
    line_children = get_line_children(line_number, line)
    for line_number in line_children:
        process_line(line_number, data[line_number])


for line_number, line in enumerate(data):
    new_calls = process_line(line_number, line)
print(process_line.calls)
