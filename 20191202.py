
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

        if inputs[i] == 1:
            indice_one = inputs[i+1]
            indice_two = inputs[i+2]
            indice_three = inputs[i+3]
            inputs[indice_three] = inputs[indice_one] + inputs[indice_two]
        elif inputs[i] == 2:
            indice_one = inputs[i+1]
            indice_two = inputs[i+2]
            indice_three = inputs[i+3]
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

    inputs = get_input_from_file('./20191202.txt')
    inputs_parsed = convert_input(inputs[0])
    inputs_parsed[1] = 66
    inputs_parsed[2] = 35
    r = walk_input(inputs_parsed)
    assert r[0] == 19690720


if __name__ == "__main__":
    # execute only if run as a script
    test_walk_input()
    output = 0

    inputs = get_input_from_file('./20191202.txt')
    tt = build_tree(convert_input(inputs[0]))

    for i in range(0, 100):
        for j in range(0, 100):
            inputs = get_input_from_file('./20191202.txt')
            inputs_parsed = convert_input(inputs[0])
            inputs_parsed[1] = i
            inputs_parsed[2] = j
            results = walk_input(inputs_parsed)
            # print('noun : {0} - verb : {1} - result : {2}'.format(i, j, results[0]))
            if results[0] == 19690720:
                print("FOUNDED ! ")
                print(i)
                print(j)
                print(100*i+j)
                print(results)
                exit()
