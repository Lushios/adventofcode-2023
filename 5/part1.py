with open("input.txt") as file:
    data = file.read().splitlines()


class ConversionRange:
    def __init__(self, destination_start, source_start, length):
        self.source_range = range(source_start, source_start + length)
        self.destination_range = range(destination_start, destination_start + length)


def convert_value(value, conversion_ranges):
    for conversion_range in conversion_ranges:
        if value in conversion_range.source_range:
            return conversion_range.destination_range[value - conversion_range.source_range.start]
    return value


def read_data(data):
    seeds_to_plant = [int(seed) for seed in data[0].split(": ")[1].split(" ")]
    conversions = {}
    conversions_string = filter(lambda x: x != '', data[2:])
    current_conversion = ''
    for conversion_line in conversions_string:
        if not conversion_line[0].isnumeric():
            current_conversion = conversion_line.split(" ")[0]
            conversions[current_conversion] = []
        else:
            conversions[current_conversion].append(ConversionRange(*[int(x) for x in conversion_line.split(" ")]))

    return seeds_to_plant, conversions


seeds, conversions = read_data(data)
final_seed_locations = []
for seed in seeds:
    seed_value = seed
    for conversion_name, conversion in conversions.items():
        seed_value = convert_value(seed_value, conversion)
    final_seed_locations.append(seed_value)
print(min(final_seed_locations))
