with open("input.txt") as file:
    data = file.read().splitlines()


low = 'low'
high = 'high'


class RXException(Exception):
    pass


def parse_data(data):
    modules = {
        'button': Button('button', ['broadcaster']),
        'output': Output('output', []),
        'rx': Output('output', []),
    }
    for line in data:
        module, destinations = line.split(' -> ')
        destinations = destinations.split(', ')
        if module.startswith('%'):
            module_name = module[1:]
            modules[module_name] = FlipFlop(module_name, destinations)
        elif module.startswith('&'):
            module_name = module[1:]
            conjunction_inputs = []
            for line2 in data:
                if module_name in line2 and line2 != line:
                    conjunction_inputs.append(line2.split(' -> ')[0][1:])
            modules[module_name] = Conjunction(module_name, destinations, conjunction_inputs)
        else:
            modules[module] = Broadcaster(module, destinations)
    return modules


class Module:
    def __init__(self, name, destinations):
        self.name = name
        self.destinations = destinations

    def receive_pulse(self, pulse, source):
        pass


class RX(Module):
    def receive_pulse(self, pulse, source):
        if pulse == low:
            raise RXException("RX cannot receive low pulses.")

class Button(Module):
    def receive_pulse(self, pulse, source):
        return [[self.destinations[0], low, self.name]]
        # raise Exception("Button cannot receive pulses.")

    # def send_pulse(self):
    #     pass
        # return [self.destinations[0], low]


class Broadcaster(Module):
    def receive_pulse(self, pulse, source):
        return [[destination, pulse, self.name] for destination in self.destinations]


class Output(Module):
    def receive_pulse(self, pulse, source):
        return []


class Conjunction(Module):
    def __init__(self, name, destinations, inputs):
        super().__init__(name, destinations)
        self.stored_pulses = {mod: low for mod in inputs}

    def receive_pulse(self, pulse, source):
        self.stored_pulses[source] = pulse
        if all(pulse == high for pulse in self.stored_pulses.values()):
            return [[destination, low, self.name] for destination in self.destinations]
        else:
            return [[destination, high, self.name] for destination in self.destinations]


class FlipFlop(Module):
    def __init__(self, name, destinations):
        super().__init__(name, destinations)
        self.isOn = False

    def receive_pulse(self, pulse, source):
        pulses = []
        if pulse == low:
            self.isOn = not self.isOn
            if self.isOn:
                pulses = [[destination, high, self.name] for destination in self.destinations]
            else:
                pulses = [[destination, low, self.name] for destination in self.destinations]
        return pulses


mods = parse_data(data)
button_presses = 1000
low_counter, high_counter = 0, 0

try:
    while True:
        impulses = []
        print(button_presses)
        impulses.append(['broadcaster', low, 'button'])
        button_presses -= 1
        for impulse in impulses:
            new_pulses = mods[impulse[0]].receive_pulse(impulse[1], impulse[2])
            impulses.extend(new_pulses)
        low_counter += len([impulse for impulse in impulses if impulse[1] == low])
        high_counter += len([impulse for impulse in impulses if impulse[1] == high])
except RXException:
    print(low_counter, high_counter)
    print(low_counter * high_counter)


print(low_counter, high_counter)
print(low_counter * high_counter)






