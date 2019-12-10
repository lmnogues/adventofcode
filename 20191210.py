import numpy as np


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
    print(coordinates)
    return coordinates


if __name__ == "__main__":
    constelation = prepare_constelation()
    coordinates = extract_coordinates(constelation)
    all_result = dict()
    x = [5, 8]
    y = [1, 7]
    z = [9, 9]

    for A in coordinates:
        eq_dict = dict()
        for B in coordinates:
            if A != B or A == B:
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
        #print("Coordinates {0} - result : {1}".format(A, len(eq_dict.keys())))

    nb_visible = 0
    max_coord = None
    for coord in all_result.keys():
        val = len(all_result[coord])
        if nb_visible < val:
            nb_visible = val
            max_coord = coord

    print("MAX Coordinates {0} - result : {1}".format(max_coord, nb_visible))
