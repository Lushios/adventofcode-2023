from itertools import cycle
from math import lcm

with open("input.txt") as file:
    data = file.read().splitlines()


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
    starting_nodes = list(filter(lambda x: x[2] == 'A', list(node_map.keys())))
    return instructions, node_map, starting_nodes


@count_calls
def travel(instruction, node_map, current_node):
    return node_map[current_node][instruction]


instructions, node_map, starting_nodes = parse_data(data)
travel_distances = []
for node in starting_nodes:
    for instruction in cycle(instructions):
        node = travel(instruction, node_map, node)
        if node[2] == 'Z':
            travel_distances.append(travel.calls)
            travel.calls = 0
            break
print(lcm(*travel_distances))
