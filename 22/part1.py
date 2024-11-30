with open("input.txt") as file:
    data = file.read().splitlines()


X = 0
Y = 1
Z = 2


def parse_data(lines):
    blocks = []
    for line in lines:
        edge_a, edge_b = line.split("~")
        edge_a = [int(x) for x in edge_a.split(',')]
        edge_b = [int(x) for x in edge_b.split(',')]
        if edge_a[Z] < edge_b[Z]:
            blocks.append((edge_a, edge_b))
        else:
            blocks.append((edge_b, edge_a))
    return blocks


def sort_blocks_vertically(blocks):
    blocks.sort(key=lambda block: block[0][Z])
    return blocks


def transform_blocks(blocks):
    new_blocks = []
    for block in blocks:
        new_block = []
        if block[0][X] > block[1][X]:  # yeah, copilot wrote this code, bite me
            for i in range(block[0][X] - block[1][X] + 1):
                new_block.append([block[1][X] + i, block[1][Y], block[1][Z]])
        elif block[0][X] < block[1][X]:
            for i in range(block[1][X] - block[0][X] + 1):
                new_block.append([block[0][X] + i, block[0][Y], block[0][Z]])
        elif block[0][Y] > block[1][Y]:
            for i in range(block[0][Y] - block[1][Y] + 1):
                new_block.append([block[1][X], block[1][Y] + i, block[1][Z]])
        elif block[0][Y] < block[1][Y]:
            for i in range(block[1][Y] - block[0][Y] + 1):
                new_block.append([block[0][X], block[0][Y] + i, block[0][Z]])
        elif block[0][Z] > block[1][Z]:
            for i in range(block[0][Z] - block[1][Z] + 1):
                new_block.append([block[1][X], block[1][Y], block[1][Z] + i])
        elif block[0][Z] < block[1][Z]:
            for i in range(block[1][Z] - block[0][Z] + 1):
                new_block.append([block[0][X], block[0][Y], block[0][Z] + i])
        new_blocks.append(new_block)
    return new_blocks


def let_the_blocks_fall(blocks):
    for block in blocks:
        blocked = False
        for coord in block:
            if [coord[X], coord[Y], coord[Z] - 1] not in block:


blocks = parse_data(data)
blocks = sort_blocks_vertically(blocks)
blocks = transform_blocks(blocks)
print(blocks)

