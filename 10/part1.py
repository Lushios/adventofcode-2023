with open("input.txt") as file:
    data = file.read().splitlines()


class Pipe:
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol


location_to_pipe = {
    (0, -1): ['|', 'F', '7', 'S'],
    (0, 1): ['|', 'L', 'J', 'S'],
    (1, 0): ['-', 'J', '7', 'S'],
    (-1, 0): ['-', 'L', 'F', 'S'],
}

pipe_to_location = {
    '|': [(0, -1), (0, 1)],
    '-': [(1, 0), (-1, 0)],
    'F': [(0, 1), (1, 0)],
    'L': [(0, -1), (1, 0)],
    'J': [(0, -1), (-1, 0)],
    '7': [(-1, 0), (0, 1)],
    'S': [(0, -1), (0, 1), (1, 0), (-1, 0)],
}


def get_adjacent_pipe(pipe: Pipe, pipe_to_ignore=None):
    adjacent_pipes = []

    directions_to_check = pipe_to_location[pipe.symbol]
    mapping = {key: value for key, value in location_to_pipe.items() if key in directions_to_check}
    for key, value in mapping.items():
        if pipe_to_ignore is not None and pipe_to_ignore.x == pipe.x + key[0] and pipe_to_ignore.y == pipe.y + key[1]:
            continue
        if data[pipe.y + key[1]][pipe.x + key[0]] in value:
            adjacent_pipes.append(Pipe(pipe.x + key[0], pipe.y + key[1], data[pipe.y + key[1]][pipe.x + key[0]]))
    return adjacent_pipes.pop()


for y, line in enumerate(data):
    x = line.find('S')
    if x != -1:
        starting_pipe = Pipe(x, y, 'S')

current_pipe = get_adjacent_pipe(starting_pipe)
loop = [starting_pipe, current_pipe]
pipe_to_ignore = starting_pipe
loop_complete = False
while not loop_complete:
    next_pipe = get_adjacent_pipe(current_pipe, pipe_to_ignore)
    pipe_to_ignore = current_pipe
    current_pipe = next_pipe
    loop.append(current_pipe)
    if current_pipe.symbol == 'S':
        loop_complete = True
print(len(loop)//2)
