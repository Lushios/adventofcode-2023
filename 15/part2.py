with open("input.txt") as file:
    data = file.read().splitlines()


class Box:
    def __init__(self, number):
        self.number = number
        self.lenses = []

    def remove_box(self, label):
        for i, lens in enumerate(self.lenses):
            if lens.label == label:
                self.lenses.pop(i)

    def add_lens(self, lens):
        updated_existing_lens = False
        for i, existing_lens in enumerate(self.lenses):
            if existing_lens.label == lens.label:
                self.lenses[i].focal_length = lens.focal_length
                updated_existing_lens = True
        if not updated_existing_lens:
            self.lenses.append(lens)

    def get_focusing_power(self):
        return sum([int(lens.focal_length) * (i+1) * self.number for i, lens in enumerate(self.lenses)])


class Lens:
    def __init__(self, label, focal_length):
        self.label = label
        self.focal_length = focal_length


def parse_data(data):
    parsed_data = []
    for line in data:
        parsed_data.extend(line.split(','))
    return parsed_data


def parse_instruction(instruction):
    if '-' in instruction:
        label, action = instruction[:-1], instruction[-1]
    else:
        label, action = instruction[:-2], instruction[-2:]
    box_number = get_instruction_hash(label)
    return label, action, box_number


def get_instruction_hash(instruction_label):
    instruction_hash = 0
    for element in instruction_label:
        instruction_hash += ord(element)
        instruction_hash *= 17
        instruction_hash %= 256
    return instruction_hash


def perform_action(instruction, boxes):
    label, action, box_number = parse_instruction(instruction)
    if action == '-':
        boxes[box_number].remove_box(label)
    else:
        focal_length = int(action[-1])
        boxes[box_number].add_lens(Lens(label, focal_length))


instructions = parse_data(data)
boxes = [Box(i + 1) for i in range(256)]
for instruction in instructions:
    perform_action(instruction, boxes)
print(sum([box.get_focusing_power() for box in boxes]))
