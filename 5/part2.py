with open("input.txt") as file:
    data = file.read().splitlines()


class ConversionRange:
    def __init__(self, destination_start, source_start, length):
        self.source_range = range(source_start, source_start + length)
        self.destination_range = range(destination_start, destination_start + length)


class Range:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def isEmpty(self):
        return self.start == self.stop


def convert_ranges(ranges, conversions):
    ranges.sort(key=lambda x: x.start)
    converted_ranges = []
    for range in ranges:
        for conversion in conversions:
            conversion_diff = conversion.destination_range.start - conversion.source_range.start
            if range.isEmpty():
                continue
            if range.start in conversion.source_range:
                where_overlap_ends = min(range.stop, conversion.source_range.stop)
                converted_ranges.append(Range(range.start + conversion_diff, where_overlap_ends + conversion_diff))
                range.start = where_overlap_ends
            elif range.start < conversion.source_range.start and range.stop > conversion.source_range.stop:
                converted_ranges.append(Range(conversion.source_range.start + conversion_diff, conversion.source_range.stop + conversion_diff))
                ranges.append(Range(conversion.source_range.stop, range.stop))
                range.stop = conversion.source_range.start
            elif range.stop in conversion.source_range:
                converted_ranges.append(Range(conversion.source_range.start + conversion_diff, range.stop + conversion_diff))
                range.stop = conversion.source_range.start
    converted_ranges.extend(ranges)
    return converted_ranges


def read_data(data):
    seeds_info = [int(seed) for seed in data[0].split(": ")[1].split(" ")]
    seed_ranges = []
    for key, seed in enumerate(seeds_info):
        if key % 2:
            continue
        seed_ranges.append(Range(seed, seed + seeds_info[key + 1]))
    conversions = {}
    conversions_string = filter(lambda x: x != '', data[2:])
    current_conversion = ''
    for conversion_line in conversions_string:
        if not conversion_line[0].isnumeric():
            current_conversion = conversion_line.split(" ")[0]
            conversions[current_conversion] = []
        else:
            conversions[current_conversion].append(ConversionRange(*[int(x) for x in conversion_line.split(" ")]))

    return seed_ranges, conversions


seed_ranges, conversion_ranges = read_data(data)
result = []
for seed_range in seed_ranges:
    new_ranges = [seed_range]
    for conversion_range_name, conversion_range in conversion_ranges.items():
        new_ranges = convert_ranges(new_ranges, conversion_range)
    result.extend(new_ranges)

result.sort(key=lambda x: x.start)
result = list(filter(lambda x: not x.isEmpty(), result))
print(result[0].start)
