
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


def calculate_total_position(planets, orbits):
    planet_position = dict()
    for p in planets:
        planet_position[p] = calculate_position(p, orbits)
    print(planet_position)
    return sum(planet_position.values())


def test_build_planets_tree():
    inputs = [['COM', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E'], ['E', 'F'], ['B', 'G'], ['G', 'H'], ['D', 'I'], ['E', 'J'], ['J', 'K'], ['K', 'L']]
    planets = list_planets(inputs)
    orbits = build_planets_tree(inputs)
    total = calculate_total_position(planets, orbits)
    assert total == 42


if __name__ == "__main__":
    test_build_planets_tree()

    inputs = get_input_from_file('20191206.txt')
    inputs = [i.split(')') for i in inputs]
    planets = list_planets(inputs)
    orbits = build_planets_tree(inputs)
    total = calculate_total_position(planets, orbits)
    print(total)
