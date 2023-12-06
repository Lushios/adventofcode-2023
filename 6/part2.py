import re

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
    return Race(int(''.join(times)), int(''.join(distances)))


race = parse_data(data)
possible_wins = race.get_number_of_wins()
print(possible_wins)
