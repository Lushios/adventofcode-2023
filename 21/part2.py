with open("input.txt") as file:
    data = file.read().splitlines()

NUMBER_OF_STEPS = 1200


def get_start_location(field):
    for y, row in enumerate(field):
        x = row.find("S")
        if x != -1:
            return x, y, 0, 0


def get_point_neighbors(point, field):
    x, y, xi, yi = point
    neighbors = []

    if x - 1 < 0 and field[y][len(field[0]) - 1] != "#":
        neighbors.append((len(field[0]) - 1, y, xi - 1, yi))
    elif field[y][x - 1] != "#":
        neighbors.append((x - 1, y, xi, yi))
    if x + 1 >= len(field[0]) and field[y][0] != "#":
        neighbors.append((0, y, xi + 1, yi))
    elif field[y][x + 1] != "#":
        neighbors.append((x + 1, y, xi, yi))
    if y - 1 < 0 and field[len(field) - 1][x] != "#":
        neighbors.append((x, len(field) - 1, xi, yi - 1))
    elif field[y - 1][x] != "#":
        neighbors.append((x, y - 1, xi, yi))
    if y + 1 >= len(field) and field[0][x] != "#":
        neighbors.append((x, 0, xi, yi + 1))
    elif field[y + 1][x] != "#":
        neighbors.append((x, y + 1, xi, yi))

    return neighbors


start = get_start_location(data)
current_points = {start}
buffer = []
while NUMBER_OF_STEPS > 0:
    print(NUMBER_OF_STEPS)
    new_points = []
    NUMBER_OF_STEPS -= 1
    for point in current_points:
        neighbors = get_point_neighbors(point, data)
        new_points.extend(neighbors)
    current_points = set(new_points)
    buffer.append(len(current_points))
with open('output2.txt', 'w') as file:
    file.write('\n'.join(map(str, buffer)))
print(len(current_points))
