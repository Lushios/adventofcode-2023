from functools import reduce

with open("input.txt") as file:
    data = file.read().splitlines()

max_y = len(data) - 1
max_x = len(data[0]) - 1


class Number:
    def __init__(self, xs, y):
        self.xs = xs
        self.y = y
        self.number = int(''.join([data[y][x] for x in xs]))

    def __eq__(self, other):
        return self.xs == other.xs and self.y == other.y

    def __hash__(self):
        return hash(''.join([str(x) for x in self.xs]) + str(self.y))

    def __str__(self):
        return f'Number: {self.number}, xs: {self.xs}, y: {self.y}'


def get_full_number(x: int, y: int):
    xs = [x]
    going_left = True
    left_counter = 1
    while going_left:
        if x - left_counter < 0:
            break
        char = data[y][x - left_counter]
        if char.isnumeric():
            xs.append(x - left_counter)
            left_counter += 1
        else:
            going_left = False
    going_right = True
    right_counter = 1
    while going_right:
        if x + right_counter > max_x:
            break
        char = data[y][x + right_counter]
        if char.isnumeric():
            xs.append(x + right_counter)
            right_counter += 1
        else:
            going_right = False
    return Number(sorted(xs), y)


def get_gear_score(x: int, y: int):
    numbers = []
    for i in range(x-1, x+2):
        if i < 0 or i > max_x:
            continue
        for j in range(y-1, y+2):
            if j < 0 or j > max_y:
                continue
            if data[j][i].isnumeric():
                number = get_full_number(i, j)
                numbers.append(number)
    all_numbers = set(numbers)
    gear_score = 0
    if len(all_numbers) == 2:
        gear_score = reduce(lambda x, y: x * y, [number.number for number in all_numbers])
    return gear_score


def process_line(line_number: int, line: str):
    line_sum = 0
    line_iter = iter(line)
    for char_number, character in enumerate(line_iter):
        if character == '*':
            gear_score = get_gear_score(char_number, line_number)
            line_sum += gear_score
    return line_sum


result = 0

for line_number, line in enumerate(data):
    result += process_line(line_number, line)
print(result)
