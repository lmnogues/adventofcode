
def get_input_from_file(file):
    with open(file, "r") as file_object:
        results = file_object.read().splitlines()
        return results


# def calculate_position_from_com(planets)
# for p in planets.key():
def list_planets(inputs):
    planets = list()
    for couple in inputs:
        if couple[0] not in planets:
            planets.append(couple[0])
        if couple[1] not in planets:
            planets.append(couple[1])
    return planets


def build_planets_tree(inputs):
    orbits = dict()
    for couple in inputs:
        orbits[couple[1]] = couple[0]
    return orbits


def calculate_position(planet, orbits):
    pos = 0
    while planet in orbits.keys():
        planet = orbits[planet]
        pos += 1
    return pos


def tree_position(planet, orbits):

    pos = list()
    while planet in orbits.keys():
        planet = orbits[planet]
        pos.append(planet)
    return pos


def calculate_total_position(planets, orbits):
    planet_position = dict()
    for p in planets:
        planet_position[p] = calculate_position(p, orbits)
    # print(planet_position)
    return planet_position


def calculate_total_tree_position(planets, orbits):
    planet_position = dict()
    for p in planets:
        planet_position[p] = tree_position(p, orbits)
    # print(planet_position)
    return planet_position


def get_maximum_position(planet_list, planet_positions):
    max_pos = 0
    for p in planet_list:
        max_pos = max(max_pos, planet_positions[p])
    return max_pos


def get_maximum_planet(planet_positions, max_pos):
    for pos in planet_positions.keys():
        if max_pos == planet_positions[pos]:
            return pos


def calculate_intersection(planets, orbits):
    planet_position = calculate_total_position(planets, orbits)
    orbit_tree = calculate_total_tree_position(planets, orbits)
    intersect = list(set(orbit_tree['YOU']) & set(orbit_tree['SAN']))
    max_pos = get_maximum_position(intersect, planet_position)
    max_plan = get_maximum_planet(planet_position, max_pos)
    result = (planet_position['YOU'] - 1 - max_pos) + (planet_position['SAN'] - 1 - max_pos)
    print("Common orbit : {0}".format(max_plan))
    return result


def test_build_planets_tree():
    inputs = [['COM', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E'], ['E', 'F'], ['B', 'G'], ['G', 'H'], ['D', 'I'], ['E', 'J'], ['J', 'K'], ['K', 'L']]
    planets = list_planets(inputs)
    orbits = build_planets_tree(inputs)
    total = sum(calculate_total_position(planets, orbits).values())
    assert total == 42

    inputs_san = [['COM', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E'], ['E', 'F'], ['B', 'G'], ['G', 'H'], ['D', 'I'], ['E', 'J'], ['J', 'K'], ['K', 'L'], ['K', 'YOU'], ['I', 'SAN']]
    planets = list_planets(inputs_san)
    orbits = build_planets_tree(inputs_san)
    result = calculate_intersection(planets, orbits)
    assert result == 4


if __name__ == "__main__":
    test_build_planets_tree()

    inputs = get_input_from_file('20191206.txt')
    inputs = [i.split(')') for i in inputs]
    planets = list_planets(inputs)
    orbits = build_planets_tree(inputs)
    total = calculate_total_position(planets, orbits)
    print(sum(total.values()))
    result = calculate_intersection(planets, orbits)
    print("total move {0}".format(result))
