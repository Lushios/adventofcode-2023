with open("input.txt") as file:
    instructions_str, details_str = file.read().split("\n\n")


def parse_instructions(instructions_string):
    instructions_string = instructions_string.split("\n")
    instructions = {}
    for instruction_str in instructions_string:
        instruction_str = instruction_str[: -1]
        instruction_name, instruction_rules_str = instruction_str.split("{")
        instruction_rules = instruction_rules_str.split(',')
        instructions[instruction_name] = instruction_rules

    return instructions


def parse_details(details_string):
    details_string = details_string.split("\n")
    details = []
    for detail_str in details_string:
        detail_str = detail_str[1: -1]
        detail_fields = detail_str.split(',')
        detail = {}
        for detail_field in detail_fields:
            field_name, field_value = detail_field.split('=')
            detail[field_name] = int(field_value)
        details.append(detail)
    return details


def follow_instruction(detail, instruction):
    for rule in instruction:
        if '<' in rule:
            condition, destination = rule.split(':')
            field, value = condition.split('<')
            if detail[field] < int(value):
                return destination
        elif '>' in rule:
            condition, destination = rule.split(':')
            field, value = condition.split('>')
            if detail[field] > int(value):
                return destination
        else:
            return rule


details, instructions = parse_details(details_str), parse_instructions(instructions_str)

for detail in details:
    detail['current_instruction'] = 'in'
    while detail['current_instruction'] not in ['A', 'R']:
        detail['current_instruction'] = follow_instruction(detail, instructions[detail['current_instruction']])


print(details)
accepted = filter(lambda detail: detail['current_instruction'] == 'A', details)
print(sum([detail['x'] + detail['m'] + detail['a'] + detail['s'] for detail in accepted]))
