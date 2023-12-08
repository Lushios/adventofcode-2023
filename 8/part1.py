from itertools import cycle

with open("input.txt") as file:
    data = file.read().splitlines()


first_node = 'AAA'
last_node = 'ZZZ'


def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper


def parse_data(data):
    instructions = data[0]
    node_map = {}
    for line in data[2:]:
        node, right_part = line.split(' = ')
        right_part = right_part.replace('(', '').replace(')', '')
        left_destination_node, right_destination_node = right_part.split(', ')
        node_map[node] = {'L': left_destination_node, 'R': right_destination_node}
    return instructions, node_map


@count_calls
def travel(instruction, node_map, current_node):
    return node_map[current_node][instruction]


instructions, node_map = parse_data(data)

current_node = first_node
for instruction in cycle(instructions):
    current_node = travel(instruction, node_map, current_node)
    if current_node == 'ZZZ':
        break

print(travel.calls)
