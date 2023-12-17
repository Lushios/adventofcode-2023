from copy import deepcopy, copy
import numpy as np

with open("input.txt") as file:
    data = file.read().splitlines()

matrix_py = []
for line in data:
    matrix_element = []
    for char in line:
        matrix_element.append(int(char))
    matrix_py.append(np.asarray(matrix_element))
map = np.asarray(matrix_py)

height = len(map)
width = len(map[0])
map[0, 0] = 0

# Initialize auxiliary arrays
directions_to_nodes = {(0, 0): ''}
distmap = np.ones((height, width), dtype=int) * np.Infinity
distmap[0, 0] = 0
originmap = np.ones((height, width), dtype=int) * np.nan
visited = np.zeros((height, width), dtype=bool)
finished = False
x, y = 0, 0

# Loop Dijkstra until reaching the target cell
while not finished:
    # only check directions not blocked by additional constraints
    # move right
    if x < width - 1:
        if (
                distmap[y][x + 1] > map[y][x + 1] + distmap[y][x]
                and not visited[y][x]
                and directions_to_nodes[(x, y)][-3:] != 'rrr'
        ):
            distmap[y][x + 1] = map[y][x + 1] + distmap[y][x]
            originmap[y][x + 1] = np.ravel_multi_index([x, y], (height, width))
            directions_to_nodes[(x + 1, y)] = directions_to_nodes[(x, y)] + 'r'
            direction = 'r'
    # move left
    if x > 0:
        if (
                distmap[y][x - 1] > map[y][x - 1] + distmap[y][x]
                and not visited[y][x - 1]
                and directions_to_nodes[(x, y)][-3:] != 'lll'
        ):
            distmap[y][x - 1] = map[y][x - 1] + distmap[y][x]
            originmap[x - 1, y] = np.ravel_multi_index([x, y], (height, width))
            directions_to_nodes[(x - 1, y)] = directions_to_nodes[(x, y)] + 'l'
            direction = 'l'
    # move down
    if y < height - 1:
        if (
                distmap[y + 1][x] > map[y + 1][x] + distmap[y][x]
                and not visited[y + 1][x]
                and directions_to_nodes[(x, y)][-3:] != 'ddd'
        ):
            distmap[y + 1][x] = map[y + 1][x] + distmap[y][x]
            originmap[y + 1][x] = np.ravel_multi_index([x, y], (height, width))
            directions_to_nodes[(x, y + 1)] = directions_to_nodes[(x, y)] + 'd'
            direction = 'd'
    # move up
    if y > 0:
        if (
                distmap[y - 1][x] > map[y - 1][x] + distmap[y][x]
                and not visited[y - 1][x]
                and directions_to_nodes[(x, y)][-3:] != 'uuu'
        ):
            distmap[y - 1][x] = map[y - 1][x] + distmap[y][x]
            originmap[y - 1][x] = np.ravel_multi_index([x, y], (height, width))
            directions_to_nodes[(x, y - 1)] = directions_to_nodes[(x, y)] + 'u'
            direction = 'u'

    visited[y][x] = True
    dismaptemp = distmap.copy()
    dismaptemp[np.where(visited)] = np.Infinity
    # now we find the shortest path so far
    minpost = np.unravel_index(np.argmin(dismaptemp), np.shape(dismaptemp))
    y, x = minpost[0], minpost[1]
    if x == width - 1 and y == height - 1:
        finished = True

print('The path length is: ' + str(distmap[height - 1, width - 1]))
print(directions_to_nodes[(height - 1, width - 1)])
