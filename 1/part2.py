with open("1/input.txt") as file:
    data = file.read().splitlines()

values = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}
for i in range(1, 10):
    values[str(i)] = str(i)

result = 0
results = []
for line in data:
    first_number = ''
    second_number = ''
    for i in range(1, len(line) + 1):
        sub_string = line[0:i]
        for value in values.keys():
            index = sub_string.find(value)
            if index >= 0:
                first_number = values[value]
        if first_number != '':
            break

    for i in range(1, len(line) + 1):
        sub_string = line[len(line) - i:]
        for value in values.keys():
            index = sub_string.find(value)
            if index >= 0:
                second_number = values[value]
        if second_number != '':
            break

    print(first_number, second_number, int(first_number + second_number), line)
    result += int(first_number + second_number)
print(result)
