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
    return rows_to_expand, columns_to_expand


def get_list_of_galaxies(universe):
    galaxies = []
    for i in range(len(universe)):
        for j in range(len(universe[0])):
            if universe[i][j] == '#':
                galaxies.append([i, j])
    return galaxies


def get_distances_to_other_galaxies(galaxy, galaxies, rows_to_multiply, columns_to_multiply):
    distances = []
    for other_galaxy in galaxies:
        if other_galaxy != galaxy:
            distance = abs(other_galaxy[0] - galaxy[0]) + abs(other_galaxy[1] - galaxy[1])
            additional_distance = (
                len([row for row in rows_to_multiply
                    if min(other_galaxy[0], galaxy[0]) < row < max(other_galaxy[0], galaxy[0])]
                ) +
                len([column for column in columns_to_multiply
                    if min(other_galaxy[1], galaxy[1]) < column < max(other_galaxy[1], galaxy[1])]
                )
            )
            distances.append(distance + additional_distance * 999999)
    return distances


universe = data
rows_to_multiply, columns_to_multiply = account_for_universe_expanding(data)
galaxies = get_list_of_galaxies(universe)
result = 0
for galaxy in galaxies:
    distances = get_distances_to_other_galaxies(galaxy, galaxies, rows_to_multiply, columns_to_multiply)
    result += sum(distances)
print(result//2)
