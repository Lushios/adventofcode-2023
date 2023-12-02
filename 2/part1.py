with open("input.txt") as file:
    data = file.read().splitlines()

limits = {
    'red': 12,
    'green': 13,
    'blue': 14,
}


def parse_line(line_to_parse: str):
    game_info, game_rules = line_to_parse.split(": ")
    game_id = game_info.split(" ")[1]
    game_rules = game_rules.split('; ')
    game_input = [game_rule.split(", ") for game_rule in game_rules]
    return game_id, game_input


def play_game(game_input):
    for hand in game_input:
        for color_in_hand in hand:
            for color_to_check in limits.keys():
                possible_number = color_in_hand.replace(' ' + color_to_check, "")
                if possible_number.isnumeric() and int(possible_number) > limits[color_to_check]:
                    return False
    return True


result = 0
for line in data:
    game_id, game_input = parse_line(line)
    is_possible = play_game(game_input)
    if is_possible:
        result += int(game_id)

print(result)