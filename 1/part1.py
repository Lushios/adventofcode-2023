with open("1/input.txt") as file:
    data = file.read().splitlines()

final_result = 0
for line in data:
    first_number = 0
    second_number = 0
    for char in line:
        if char.isnumeric():
            first_number = char
            break
    for char in line[::-1]:
        if char.isnumeric():
            second_number = char
            break
    final_result += int(first_number + second_number)
print(final_result)
