import requests


def get_input_from_file(file):
    with open(file, "r") as file_object:
        results = file_object.read().splitlines()
        print(results)
        return results


def calculate_day_one(inputs):
    total_fuel = 0
    for mass in inputs:
        total_fuel = total_fuel + int(int(mass)/3) - 2
    return total_fuel


def test_calculate_day_one():
    test_list = list()
    test_list.append('12')
    assert calculate_day_one(test_list) == 2
    test_list.clear()
    test_list.append('14')
    assert calculate_day_one(test_list) == 2
    test_list.clear()
    test_list.append('1969')
    assert calculate_day_one(test_list) == 654
    test_list.clear()
    test_list.append('100756')
    assert calculate_day_one(test_list) == 33583


def main():
    print("starting")
    inputs = get_input_from_file('./20191201.txt')
    day_one_total_mass = calculate_day_one(inputs)
    print(day_one_total_mass)


if __name__ == "__main__":
    # execute only if run as a script
    test_calculate_day_one()
    main()
