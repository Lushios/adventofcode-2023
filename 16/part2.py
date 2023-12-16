from copy import copy

with open("input.txt") as file:
    data = file.read().splitlines()


class Point:
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol
        self.energized = False
        self.reflections = []  # holds directions from which the beams came to the mirror


class Beam:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def get_next_point_coords(self):
        if self.direction == 'right':
            return self.x + 1, self.y
        elif self.direction == 'left':
            return self.x - 1, self.y
        elif self.direction == 'up':
            return self.x, self.y - 1
        elif self.direction == 'down':
            return self.x, self.y + 1

    def set_coords(self, x, y):
        self.x = x
        self.y = y


class Game:
    def __init__(self, playing_field, starting_beam: Beam):
        self.width = len(playing_field[0])
        self.height = len(playing_field)
        self.points = []
        for y, line in enumerate(playing_field):
            points_line = []
            for x, symbol in enumerate(line):
                points_line.append(Point(x, y, symbol))
            self.points.append(points_line)
        self.beams = [starting_beam]
        self.points[starting_beam.y][starting_beam.x].energized = True

    def tick(self):
        new_beams = []
        for beam in self.beams:
            next_point_x, next_point_y = beam.get_next_point_coords()
            if not self.coords_valid(next_point_x, next_point_y, beam.direction):
                continue
            new_beams.extend(self.process_beam_movement(beam, next_point_x, next_point_y))
        if new_beams:
            self.beams = new_beams
            return True
        else:
            return False

    def process_beam_movement(self, beam, next_point_x, next_point_y):
        beam.set_coords(next_point_x, next_point_y)
        self.points[next_point_y][next_point_x].energized = True
        resulting_beams = []
        next_point = self.points[next_point_y][next_point_x]
        if next_point.symbol == '.':
            return [beam]
        else:
            self.points[next_point_y][next_point_x].reflections.append(beam.direction)
            if next_point.symbol == '/':
                if beam.direction == 'right':
                    beam.direction = 'up'
                elif beam.direction == 'left':
                    beam.direction = 'down'
                elif beam.direction == 'up':
                    beam.direction = 'right'
                elif beam.direction == 'down':
                    beam.direction = 'left'
            elif next_point.symbol == '\\':
                if beam.direction == 'right':
                    beam.direction = 'down'
                elif beam.direction == 'left':
                    beam.direction = 'up'
                elif beam.direction == 'up':
                    beam.direction = 'left'
                elif beam.direction == 'down':
                    beam.direction = 'right'
            elif next_point.symbol == '|':
                if beam.direction in ['left', 'right']:
                    new_beam = copy(beam)
                    beam.direction = 'up'
                    new_beam.direction = 'down'
                    resulting_beams.append(new_beam)
            elif next_point.symbol == '-':
                if beam.direction in ['up', 'down']:
                    new_beam = copy(beam)
                    beam.direction = 'right'
                    new_beam.direction = 'left'
                    resulting_beams.append(new_beam)
            resulting_beams.append(beam)
            return resulting_beams

    def coords_valid(self, x, y, direction):
        return 0 <= x < self.width and 0 <= y < self.height and direction not in self.points[y][x].reflections

    def get_results(self):
        return sum([sum([1 if point.energized else 0 for point in line]) for line in self.points])


def beam_generator(width, height):
    for y in range(height):
        yield Beam(0, y, 'right')
        yield Beam(width - 1, y, 'left')
    for x in range(width):
        yield Beam(x, 0, 'down')
        yield Beam(x, height - 1, 'up')


game_results = []
for starting_beam in beam_generator(len(data[0]), len(data)):
    game = Game(data, starting_beam)
    while game.tick():
        pass
    game_results.append(game.get_results())
print(max(game_results))
