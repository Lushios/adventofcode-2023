with open("input.txt") as file:
    data = file.read().splitlines()


def parse_data(data):
    parsed_data = []
    for line in data:
        parsed_data.extend(line.split(','))
    return parsed_data


def get_instruction_hash(instruction):
    instruction_hash = 0
    for element in instruction:
        instruction_hash += ord(element)
        instruction_hash *= 17
        instruction_hash %= 256
    return instruction_hash


instructions = parse_data(data)
result = 0
for instruction in instructions:
    result += get_instruction_hash(instruction)
print(result)
