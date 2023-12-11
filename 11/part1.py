with open("input.txt") as file:
    data = file.read().splitlines()


def account_for_universe_expanding(universe):
    rows_to_expand = []
    columns_to_expand = []
    for i in range(len(data)):  # yeah, yeah I checked they're the same length
        if not any([star == '#' for star in universe[i]]):
            rows_to_expand.append(i)
        if not any([row[i] == '#' for row in universe]):
            columns_to_expand.append(i)
    for correction, row_number in enumerate(rows_to_expand):
        universe.insert(row_number + correction, '.' * len(universe[0]))
    for correction, column_number in enumerate(columns_to_expand):
        for i in range(len(universe)):
            universe[i] = universe[i][:column_number + correction] + '.' + universe[i][column_number + correction:]
    return universe


def get_list_of_galaxies(universe):
    galaxies = []
    for i in range(len(universe)):
        for j in range(len(universe[0])):
            if universe[i][j] == '#':
                galaxies.append([i, j])
    return galaxies


def get_distances_to_other_galaxies(galaxy, galaxies):
    return [
        abs(other_galaxy[0] - galaxy[0]) + abs(other_galaxy[1] - galaxy[1])
        for other_galaxy in galaxies if other_galaxy != galaxy
    ]


new_universe = account_for_universe_expanding(data)
galaxies = get_list_of_galaxies(new_universe)
result = 0
for galaxy in galaxies:
    distances = get_distances_to_other_galaxies(galaxy, galaxies)
    result += sum(distances)
print(result//2)  # man I can't do this optimal shit today
