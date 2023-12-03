with open("input.txt") as file:
    data = file.read().splitlines()

max_y = len(data) - 1
max_x = len(data[0]) - 1
print(max_x)


def check_if_number_is_valid(x1: int, x2: int, y: int, number):
    possible_xs = [*range(x1 - 1, x2 + 1)]
    possible_ys = [*range(y - 1, y + 2)]
    xs = list(filter(lambda x: 0 <= x <= max_x, possible_xs))
    ys = list(filter(lambda y: 0 <= y <= max_y, possible_ys))
    number_valid = False
    for x in xs:
        for y in ys:
            if not data[y][x].isnumeric() and data[y][x] != '.':
                number_valid = True
    return number_valid


def process_line(line_number: int, line: str):
    line_sum = 0
    line_iter = iter(line)
    # ok so I advance the iterator with the next function BUT IT DOESN'T ADVANCE THE CHAR_NUMBER
    # I should have folded at this point and tried a different way, but I got stubborn, so I use this correction var
    correction = 0
    for char_number, character in enumerate(line_iter):
        if character.isnumeric():
            end_of_number = False
            number_length = 1
            while end_of_number is False:
                if (
                        char_number + correction + number_length < len(line)
                        and line[char_number + number_length + correction].isnumeric()
                ):
                    number_length += 1
                else:
                    end_of_number = True
                    for i in range(number_length - 1):
                        next(line_iter)
            number_left_edge = char_number + correction
            number_right_edge = char_number + correction + number_length
            number = line[number_left_edge:number_right_edge]
            correction += number_length - 1
            valid = check_if_number_is_valid(number_left_edge, number_right_edge, line_number, number)
            if valid:
                print(number)
                line_sum += int(number)
    print(line_number, line_sum)
    return line_sum


result = 0
for line_number, line in enumerate(data):
    result += process_line(line_number, line)
print(result)
