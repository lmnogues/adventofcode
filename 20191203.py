import numpy
import matplotlib.pyplot as plt


def get_input_from_file(file):
    with open(file, "r") as file_object:
        results = file_object.read().splitlines()
        return results


central_point = (1, 1)


def build_vector(wire_string):
    x = central_point[0]
    y = central_point[1]
    wire_coordinates = list()
    for instruction in wire_string:
        direction = instruction[0]
        lenght = instruction[1:]
        for i in range(int(lenght)):
            if direction == 'R':
                x += 1
            if direction == 'L':
                x -= 1
            if direction == 'U':
                y += 1
            if direction == 'D':
                y -= 1
            wire_coordinates.append((x, y))
    return wire_coordinates


def distance_to_crossing(wire_string, intersection):
    x = central_point[0]
    y = central_point[1]
    distance = 0
    intersection_distance = dict()
    for instruction in wire_string:
        direction = instruction[0]
        lenght = instruction[1:]
        for i in range(int(lenght)):
            if direction == 'R':
                x += 1
            if direction == 'L':
                x -= 1
            if direction == 'U':
                y += 1
            if direction == 'D':
                y -= 1
            distance += 1
            if (x, y) in intersection:
                intersection_distance[(x, y)] = distance
    return intersection_distance


def plot_wire(positions, wire_name):
    x = []
    y = []
    for p in positions:
        x.append(p[0])
        y.append(p[1])
    plt.plot(x, y, label=wire_name)


def manhattan_distance(coordinates):
    return abs(coordinates[0] - central_point[0]) + abs(coordinates[1] - central_point[1])


def wire_intersection(wire_1, wire_2):
    return list(set(wire_1) & set(wire_2))


def calculate_min_distance(intersections):
    min_distance = float('inf')
    for intersection in intersections:
        distance = manhattan_distance(intersection)
        min_distance = min(min_distance, distance)
        print('Coordinates : {0} - distance to central point : {1}'.format(intersection, distance))
    print('Minimal distance : {0}'.format(min_distance))
    return min_distance


def calculate_combine_min_step(wire_1_distance, wire_2_distance):
    results = dict()
    for key in wire_1_distance.keys():
        distance = wire_1_distance[key] + wire_2_distance[key]
        results[key] = distance
        print('Coordinates : {0} - distance by step to central point : {1}'.format(key, distance))
    min_step = min([x for x in results.values()])
    print('Minimal distance : {0}'.format(min_step))
    return min_step


def test_build_vector():
    wire_string = ['R8', 'U5', 'L5', 'D3']
    position_1 = build_vector(wire_string)
    wire_string_2 = ['U7', 'R6', 'D4', 'L4']
    position_2 = build_vector(wire_string_2)
    intersections = wire_intersection(position_1, position_2)
    dist = calculate_min_distance(intersections)
    assert dist == 6
    w1_crossing_distance = distance_to_crossing(wire_string, intersections)
    w2_crossing_distance = distance_to_crossing(wire_string_2, intersections)
    min_dist = calculate_combine_min_step(w1_crossing_distance, w2_crossing_distance)
    assert min_dist == 30
    w1_string = ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72']
    w2_string = ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']
    w1 = build_vector(w1_string)
    w2 = build_vector(w2_string)
    intersections = wire_intersection(w1, w2)
    dist = calculate_min_distance(intersections)
    assert dist == 159
    w1_crossing_distance = distance_to_crossing(w1_string, intersections)
    w2_crossing_distance = distance_to_crossing(w2_string, intersections)
    min_dist = calculate_combine_min_step(w1_crossing_distance, w2_crossing_distance)
    assert min_dist == 610

    w3_string = ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51']
    w4_string = ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']
    w3 = build_vector(w3_string)
    w4 = build_vector(w4_string)
    intersections = wire_intersection(w3, w4)
    dist = calculate_min_distance(intersections)
    assert dist == 135
    w1_crossing_distance = distance_to_crossing(w3_string, intersections)
    w2_crossing_distance = distance_to_crossing(w4_string, intersections)
    min_dist = calculate_combine_min_step(w1_crossing_distance, w2_crossing_distance)
    assert min_dist == 410


if __name__ == "__main__":
    # x = numpy.arange(0, 10, 0.2)
    # y = numpy.sin(x)
    # fig, ax = plt.subplots()
    # ax.plot(x, y)
    # plt.show()
    test_build_vector()
    wires = get_input_from_file('20191203.txt')
    w1 = build_vector(wires[0].split(','))
    w2 = build_vector(wires[1].split(','))
    intersections = wire_intersection(w1, w2)
    dist = calculate_min_distance(intersections)

    w1_dist = distance_to_crossing(wires[0].split(','), intersections)
    w2_dist = distance_to_crossing(wires[1].split(','), intersections)
    min_step = calculate_combine_min_step(w1_dist, w2_dist)

    plot_wire(w1, 'w1')
    plot_wire(w2, 'w2')

    plt.show()
