with open("input.txt") as file:
    data = file.read().splitlines()


def get_line_answer(line_forms):
    line_answer = 0
    for line in line_forms:
        line_answer += line[-1]
    return line_answer


def get_next_line_form(line):
    result = []
    for i in range(len(line) - 1):
        result.append(line[i + 1] - line[i])
    return result


answer = 0
for line in data:
    line_forms = [[int(x) for x in line.split(' ')]]
    line_reached_final_form = False
    while not line_reached_final_form:
        new_line_form = get_next_line_form(line_forms[-1])
        line_forms.append(new_line_form)
        if all([x == 0 for x in new_line_form]):
            line_reached_final_form = True
    answer += get_line_answer(line_forms)
print(answer)
