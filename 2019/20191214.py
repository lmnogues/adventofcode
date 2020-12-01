import re
import math
from collections import defaultdict

regex_extract = r'(?P<q>\d+) (?P<ore>\w+)'


def calculate_product(chemical_reactions, fuel_needed):
    product_queue = ['FUEL']
    chemical_required = defaultdict(int)
    chemical_required['FUEL'] = fuel_needed

    while product_queue:
        current_prod = product_queue.pop()
        for reaction, parts in chemical_reactions.items():
            if reaction[1] == current_prod:
                quantity = reaction[0]
                required = math.ceil(chemical_required[current_prod] / quantity)
                for p in parts:
                    chemical_required[p[1]] += required * p[0]
                    if chemical_required[current_prod] > 0:
                        product_queue.append(p[1])
                chemical_required[current_prod] -= required * quantity

     # print(chemical_required)
    return chemical_required


def prepare_reactions(inputs):
    chemical_reactions = {}
    for line in inputs:
        extracted_data = re.findall(regex_extract, line)
        result = extracted_data[-1:][0]
        components = extracted_data[:-1]
        list_comp = []
        result = (int(result[0]), result[1])
        for c in components:
            list_comp.append((int(c[0]), c[1]))
        chemical_reactions[result] = list_comp
   # print(chemical_reactions)
    return chemical_reactions


def get_input_from_file(file):
    with open(file, "r") as file_object:
        results = file_object.read().splitlines()
        return results


if __name__ == "__main__":
    inputs = {"10 ORE => 10 A",
              "1 ORE => 1 B",
              "7 A, 1 B => 1 C",
              "7 A, 1 C => 1 D",
              "7 A, 1 D => 1 E",
              "7 A, 1 E => 1 FUEL"}
    chemical_reactions = prepare_reactions(inputs)
    result = calculate_product(chemical_reactions, 1)['ORE']
    assert result == 31

    inputs = {
        "9 ORE => 2 A",
        "8 ORE => 3 B",
        "7 ORE => 5 C",
        "3 A, 4 B => 1 AB",
        "5 B, 7 C => 1 BC",
        "4 C, 1 A => 1 CA",
        "2 AB, 3 BC, 4 CA => 1 FUEL"
    }

    chemical_reactions = prepare_reactions(inputs)
    result = calculate_product(chemical_reactions, 1)['ORE']
    assert result == 165

    inputs = get_input_from_file('./20191214.txt')
    chemical_reactions = prepare_reactions(inputs)
    ore_needed = calculate_product(chemical_reactions, 1)['ORE']
    print(result)

    max_ORE = 1000000000000
    low_fuel = max_ORE // ore_needed
    max_fuel = max_ORE-1

    print(f'{max_ORE:,}')
    while low_fuel < max_fuel:
        avg_fuel = (max_fuel + low_fuel)//2
        if low_fuel == avg_fuel:
            break
        needed = calculate_product(chemical_reactions, avg_fuel)['ORE']
        if needed < max_ORE:
            low_fuel = avg_fuel+1
        else:
            max_fuel = avg_fuel - 1

    print(f'{low_fuel:,}')
    print(low_fuel)
