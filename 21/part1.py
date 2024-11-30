with open("input.txt") as file:
    data = file.read().splitlines()

NUMBER_OF_STEPS = 64


def get_start_location(field):
    for y, row in enumerate(field):
        x = row.find("S")
        if x != -1:
            return x, y


def get_point_neighbors(point, field):
    x, y = point
    neighbors = []
    if x > 0 and field[y][x-1] != "#":
        neighbors.append((x-1, y))
    if x < len(field[0]) - 1 and field[y][x+1] != "#":
        neighbors.append((x+1, y))
    if y > 0 and field[y-1][x] != "#":
        neighbors.append((x, y-1))
    if y < len(field) - 1 and field[y+1][x] != "#":
        neighbors.append((x, y+1))
    return neighbors


start = get_start_location(data)
current_points = {start}
while NUMBER_OF_STEPS > 0:
    new_points = []
    NUMBER_OF_STEPS -= 1
    for point in current_points:
        neighbors = get_point_neighbors(point, data)
        new_points.extend(neighbors)
    current_points = set(new_points)
print(len(current_points))
