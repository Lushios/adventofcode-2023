import numpy as np
import sys

with open("input.txt") as file:
    data = file.read().splitlines()


directions_mapping = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, -1),
    'D': (0, 1)
}


def parse_line(line):
    direction, blocks_number, _ = line.split(' ')
    return direction, int(blocks_number)


def get_neighbors(start_coordinate, trench_map):
    # trench_map[start_coordinate[1]][start_coordinate[0]] = 'X'
    neighbors = []
    left_coordinates = (start_coordinate[0] - 1, start_coordinate[1])
    right_coordinates = (start_coordinate[0] + 1, start_coordinate[1])
    up_coordinates = (start_coordinate[0], start_coordinate[1] - 1)
    down_coordinates = (start_coordinate[0], start_coordinate[1] + 1)
    for coordinates in [left_coordinates, right_coordinates, up_coordinates, down_coordinates]:
        if (
                trench_map.shape[1] - 1 >= coordinates[0] >= 0
                and trench_map.shape[0] - 1 >= coordinates[1] >= 0
                and trench_map[coordinates[1]][coordinates[0]] == '.'
        ):
            neighbors.append(coordinates)
    # for neighbor in neighbors:
    #     clear_field(neighbor, trench_map)
    print(len(neighbors))
    return neighbors


instructions = [[direction, blocks_number] for direction, blocks_number in map(parse_line, data)]
current_coordinate = (0, 0)
trench_coordinates = [current_coordinate]
for instruction in instructions:
    direction, blocks_number = instruction
    for i in range(blocks_number):
        current_coordinate = tuple(map(lambda x, y: x + y, current_coordinate, directions_mapping[direction]))
        trench_coordinates.append(current_coordinate)
min_x = min(trench_coordinates, key=lambda x: x[0])[0]
min_y = min(trench_coordinates, key=lambda x: x[1])[1]
trench_coordinates = list(map(lambda x: (x[0] - min_x, x[1] - min_y), trench_coordinates))

max_x = max(trench_coordinates, key=lambda x: x[0])[0]
max_y = max(trench_coordinates, key=lambda x: x[1])[1]
print(trench_coordinates)
print(max_x)
print(max_y)

trench_map = np.empty((max_y + 1, max_x + 1), dtype=str)
trench_map.fill('.')
for coordinate in trench_coordinates:
    trench_map[coordinate[1], coordinate[0]] = '#'

sys.setrecursionlimit(100000)
coordinates = [(0, 0), (max_x, 0), (0, max_y), (max_x, max_y)]
i = 0
for coordinate in coordinates:
    print(i := i+1)
    trench_map[coordinate[1]][coordinate[0]] = 'X'
    neighbors = get_neighbors(coordinate, trench_map)
    for neighbor in neighbors:
        if neighbor not in coordinates:
            coordinates.append(neighbor)

with open('trench.txt', 'w') as file:
    for line in trench_map:
        file.write(''.join(line) + '\n')

result = 0
for line in trench_map:
    line_result = line.tolist().count('#') + line.tolist().count('.')
    result += line_result
print(result)
