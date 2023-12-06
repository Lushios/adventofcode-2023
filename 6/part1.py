import re
from functools import reduce

with open("input.txt") as file:
    data = file.read().splitlines()

number_pattern = re.compile(r"\d+")


class Race:
    def __init__(self, time, distance):
        self.time = time
        self.distance = distance

    def get_number_of_wins(self):
        best_time = int(round(self.time / 2))
        possible_wins = 0
        for i in range(best_time, self.time):
            if i * (self.time - i) > self.distance:
                possible_wins += 1
            else:
                break
        possible_wins *= 2
        if self.time % 2 == 0:
            possible_wins -= 1
        return possible_wins


def parse_data(data):
    times = number_pattern.findall(data[0])
    distances = number_pattern.findall(data[1])
    return [Race(int(times[i]), int(distances[i])) for i in range(len(times))]


races = parse_data(data)
possible_wins = []
for race in races:
    possible_wins.append(race.get_number_of_wins())
print(reduce(lambda x, y: x * y, possible_wins))
