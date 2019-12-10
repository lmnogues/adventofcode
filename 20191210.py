import numpy as np
import math


def get_input_from_file(file):
    with open(file, "r") as file_object:
        results = file_object.read().splitlines()
        return results


def get_slope(A, B):
    # y = mx+b
    x_dist = float(B[0]*1.0 - A[0]*1.0)
    y_dist = float(B[1]*1.0 - A[1]*1.0)
    if x_dist == 0:
        return 0.
    return float(y_dist/x_dist)


def get_y_intercetp(A, B, slope):
    # y = mx+b
    # b = y-mx
    if(slope == 0) and A[0] == B[0]:
        # equation is X=n
        return A[0]
    return float(A[1] - slope * A[0])


def get_equation(A, B):
    slope = get_slope(A, B)
    yIntercept = get_y_intercetp(A, B, slope)
    equation = "y = {0}x+{1}".format(slope, yIntercept)
    # y = mx+b
    return equation


def prepare_constelation():
    inputs = get_input_from_file('./20191210.txt')
    const = list()
    for line in inputs:
        x = list()
        for i in line:
            if i == '.':
                x.append(" ")
            else:
                x.append("#")
        const.append(x)
    constelation = np.asarray(const)
    print(constelation)
    return constelation


def extract_coordinates(constelation):
    ii = np.where(constelation == '#')
    coordinates = tuple(zip(ii[1], ii[0]))
    # print(coordinates)
    return coordinates


def determine_monitoring_position(coordinates):
    all_result = dict()
    for A in coordinates:
        eq_dict = dict()
        for B in coordinates:
            eq = get_equation(A, B)
            distance = (A[0] - B[0]) + (A[1] - B[1])
            dir = 1
            if distance < 0:
                dir = 0
            elif distance > 0:
                dir = 2

            list_coord = eq_dict.get(eq)
            key = (eq, dir)
            if list_coord == None:
                list_coord = list()
            list_coord.append(B)
            eq_dict[key] = list_coord
        all_result[A] = eq_dict
        # print("Coordinates {0} - result : {1}".format(A, len(eq_dict.keys())))

    nb_visible = 0
    max_coord = None
    for coord in all_result.keys():
        val = len(all_result[coord])
        if nb_visible < val:
            nb_visible = val
            max_coord = coord

    print("MAX Coordinates {0} - result : {1}".format(max_coord, nb_visible))
    return all_result[max_coord], max_coord


def calculate_angles(station, asteroids):

    asteroid_angles = dict()
    for asteroid in asteroids:
        x = asteroid[0]
        y = asteroid[1]
        cx = station[0]
        cy = station[1]
        calc = math.atan2((x - cx), (y - cy))
        asteroid_angles[asteroid] = calc
    s = [(k, asteroid_angles[k]) for k in sorted(asteroid_angles, key=asteroid_angles.get, reverse=True)]
    return s


if __name__ == "__main__":
    constelation = prepare_constelation()
    coordinates = extract_coordinates(constelation)
    equation_planets, max_coord = determine_monitoring_position(coordinates)
    print(max_coord)
    asteroid_to_destroy = list()
    for equation in equation_planets:
        for coord in equation_planets[equation]:
            if coord != max_coord and coord not in asteroid_to_destroy:
                asteroid_to_destroy.append(coord)
    # print(asteroid_to_destroy)
    # print(len(asteroid_to_destroy))
    asteroid_to_destroy_sorted = calculate_angles(max_coord, asteroid_to_destroy)
    count = 2
    for aste in asteroid_to_destroy_sorted:
        print(count, aste)
        if count == 200:
            exit()
        count += 1
