with open("input.txt") as file:
    data = file.read().splitlines()


def find_new_boulder_location(field, boulder_coords, direction):
    boulder_has_arrived = False
    while not boulder_has_arrived:
        if (boulder_coords[0] + direction[0] < 0 or boulder_coords[0] + direction[0] > len(field[0]) - 1
                or boulder_coords[1] + direction[1] < 0 or boulder_coords[1] + direction[1] > len(field) - 1):
            boulder_has_arrived = True
        else:
            new_coords = (boulder_coords[0] + direction[0], boulder_coords[1] + direction[1])
            if field[new_coords[1]][new_coords[0]] == '.':
                boulder_coords = new_coords
            else:
                boulder_has_arrived = True
    return boulder_coords


def get_ranges_by_direction(direction, field):
    if direction == (0, -1) or direction == (-1, 0):
        return range(len(field)), range(len(field[0]))
    elif direction == (0, 1):
        return range(len(field) - 1, -1, -1), range(len(field[0]))
    elif direction == (1, 0):
        return range(len(field)), range(len(field[0]) - 1, -1, -1)


def tilt_the_field(field, direction):
    i_range, j_range = get_ranges_by_direction(direction, field)
    for i in i_range:
        for j in j_range:
            if field[i][j] != "O":
                continue
            else:
                x, y = find_new_boulder_location(field, (j, i), direction)
                field[i] = field[i][:j] + "." + field[i][j + 1:]
                field[y] = field[y][:x] + "O" + field[y][x + 1:]
    return field


def calculate_pressure(field):
    result = 0
    for i, line in enumerate(field):
        result += line.count('O') * (len(field) - i)
    return result


#  ok so the story goes like this: I've discovered that from a certain point the pressure repeats itself every 38 runs
#  consistently, so I just printed the dictionary of the first 1000 runs and then calculated the relevant lower than
#  a billion run number and that was the answer. I'm SO LAZY I don't wanna code this part(
for i in range(999999999, 500, -380):
    print(i)

field = data
debug_dict = {}
for i in range(1):
    print('run ' + str(i))
    for direction in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
        field = tilt_the_field(field, direction)
    pressure = calculate_pressure(field)
    print('pressure ' + str(pressure))
    debug_dict[i] = pressure
with open('output.txt', 'w') as file:
    for line in field:
        file.write(line + '\n')
pressure = calculate_pressure(field)
print(debug_dict)
with open('output1.txt', 'w') as file:
    for key, value in debug_dict.items():
        file.write(str(key) + ' | ' + str(value) + '\n')
