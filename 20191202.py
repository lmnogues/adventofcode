
def get_input_from_file(file):
    with open(file, "r") as file_object:
        results = file_object.read().splitlines()
        return results


def convert_input(inputs):
    split_inputs = inputs.split(',')
    results = list()
    for s in split_inputs:
        results.append(int(s))
    return results


def walk_input(inputs):
    for i in range(0, len(inputs) - 1, 4):
        if inputs[i] == 99:
            break

        indice_one = inputs[i+1]
        indice_two = inputs[i+2]
        indice_three = inputs[i+3]

        if inputs[i] == 1:
            inputs[indice_three] = inputs[indice_one] + inputs[indice_two]
        elif inputs[i] == 2:
            inputs[indice_three] = inputs[indice_one] * inputs[indice_two]

    return inputs


def input_as_text(inputs):
    return ','.join((str(x) for x in inputs))


def test_walk_input():

    r = walk_input([1, 0, 0, 0, 99])
    r = input_as_text(r)
    assert r == '2,0,0,0,99'

    r = walk_input([2, 3, 0, 3, 99])
    r = input_as_text(r)
    assert r == '2,3,0,6,99'

    r = walk_input([2, 4, 4, 5, 99, 0])
    r = input_as_text(r)
    assert r == '2,4,4,5,99,9801'

    r = walk_input([1, 1, 1, 4, 99, 5, 6, 0, 99])
    r = input_as_text(r)
    assert r == '30,1,1,4,2,5,6,0,99'


if __name__ == "__main__":
    # execute only if run as a script
    test_walk_input()
    inputs = get_input_from_file('./20191202.txt')
    print(inputs[0])
    inputs_parsed = convert_input(inputs[0])
    inputs_parsed[1] = 12
    inputs_parsed[2] = 2
    results = walk_input(inputs_parsed)
    print(results[0])
