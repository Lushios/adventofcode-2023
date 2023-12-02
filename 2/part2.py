from functools import reduce

with open("input.txt") as file:
    data = file.read().splitlines()


def parse_line(line_to_parse: str):
    game_info, game_rules = line_to_parse.split(": ")
    game_rules = game_rules.split('; ')

    def parse_rule(rule):
        colors_with_numbers = rule.split(", ")
        color_dict = (
            {
                color: int(number)
                for number, color in [
                    color_with_number.split(" ") for color_with_number in colors_with_numbers
                ]
            }
        )
        return color_dict

    game_input = list(map(parse_rule, game_rules))
    return game_input


def play_game(game_input):
    min_possible_kubiki = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }

    for hand in game_input:
        for color, number in hand.items():
            if number > min_possible_kubiki[color]:
                min_possible_kubiki[color] = number
    return reduce(lambda x, y: x*y, min_possible_kubiki.values())


result = 0
for line in data:
    game_input = parse_line(line)
    game_result = play_game(game_input)
    result += game_result

print(result)