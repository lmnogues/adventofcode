import requests


def get_input_from_file(file):
    with open(file, "r") as file_object:
        results = file_object.read().splitlines()
        return results


def calculate_day_one_part_one(inputs):
    total_fuel = 0
    for mass in inputs:
        total_fuel = total_fuel + int(int(mass)/3) - 2
    return total_fuel


def calculate_day_two_fuel(mass):
    return max(0, int(int(mass)/3) - 2)


def calculate_day_one_part_two(inputs):
    total_fuel = 0
    for mass in inputs:
        fuel_for_mass = calculate_day_two_fuel(mass)
        total_fuel = total_fuel + fuel_for_mass
        while fuel_for_mass > 0:
            fuel_for_mass = calculate_day_two_fuel(fuel_for_mass)
            total_fuel = total_fuel + fuel_for_mass
    return total_fuel


def test_calculate_day_one_part_one():
    test_list = list()

    test_list.append('12')
    r = calculate_day_one_part_one(test_list)
    assert r == 2
    test_list.clear()

    test_list.append('14')
    r = calculate_day_one_part_one(test_list)
    assert r == 2
    test_list.clear()

    test_list.append('1969')
    r = calculate_day_one_part_one(test_list)
    assert r == 654
    test_list.clear()

    test_list.append('100756')
    r = calculate_day_one_part_one(test_list)
    assert r == 33583


def test_calculate_day_one_part_two():
    test_list = list()

    test_list.append('14')
    r = calculate_day_one_part_two(test_list)
    assert r == 2
    test_list.clear()

    test_list.append('1969')
    r = calculate_day_one_part_two(test_list)
    assert r == 966
    test_list.clear()

    test_list.append('100756')
    r = calculate_day_one_part_two(test_list)
    assert r == 50346


if __name__ == "__main__":
    # execute only if run as a script
    print("validating")
    test_calculate_day_one_part_one()
    test_calculate_day_one_part_two()
    print("processing days")
    inputs = get_input_from_file('./20191201.txt')
    day_one_total_mass = calculate_day_one_part_one(inputs)
    print(day_one_total_mass)
    day_two_total_mass = calculate_day_one_part_two(inputs)
    print(day_two_total_mass)
