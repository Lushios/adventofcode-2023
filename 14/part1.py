with open("input.txt") as file:
    data = file.read().splitlines()


def find_new_boulder_location(field, y, x):
    boulder_has_arrived = False
    while not boulder_has_arrived:
        if y != 0 and field[y - 1][x] == '.':
            y -= 1
        else:
            boulder_has_arrived = True
    return y, x


def tilt_the_field(field):
    for i in range(1, len(field)):
        for j in range(len(field[0])):
            if field[i][j] != "O":
                continue
            else:
                y, x = find_new_boulder_location(field, i, j)
                field[i] = field[i][:j] + "." + field[i][j + 1:]
                field[y] = field[y][:x] + "O" + field[y][x + 1:]
    return field


def calculate_pressure(field):
    result = 0
    for i, line in enumerate(field):
        result += line.count('O') * (len(field) - i)
    return result


tilted_field = tilt_the_field(data)
with open('output.txt', 'w') as file:
    for line in tilted_field:
        file.write(line + '\n')
pressure = calculate_pressure(tilted_field)
print(pressure)
