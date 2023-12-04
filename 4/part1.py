from math import pow

with open("input.txt") as file:
    data = file.read().splitlines()


def get_numbers_from_string(string: str):
    return [int(number.strip()) for number in string.split(' ') if number]


def process_line(line: str):
    left_part, right_part = line.split(' | ')
    winning_numbers = get_numbers_from_string(left_part.split(': ')[1])
    actual_numbers = get_numbers_from_string(right_part)
    intersection = [number for number in winning_numbers if number in actual_numbers]
    line_score = int(pow(2, len(intersection) - 1))
    return line_score


total_score = 0
for line in data:
    line_score = process_line(line)
    total_score += line_score
print(total_score)
