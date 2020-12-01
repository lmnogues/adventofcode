
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


returned_values = list()


def walk_input(inputs, opCode3_input):
    i = 0
    returned_values.clear()
    while inputs[i] != 99:
        instr = f"{inputs[i]:05}"
        opCode = instr[-2:]
        paramCode_param1 = instr[2]
        paramCode_param2 = instr[1]
        paramCode_param3 = instr[0]

        if opCode in ['01', '02', '04', '05', '06', '07', '08']:
            if paramCode_param1 == '0':
                valueA = inputs[inputs[i+1]]
            elif paramCode_param1 == '1':
                valueA = inputs[i+1]

            if opCode in ['01', '02', '05', '06', '07', '08']:
                if paramCode_param2 == '0':
                    valueB = inputs[inputs[i+2]]
                elif paramCode_param2 == '1':
                    valueB = inputs[i+2]

                if opCode in []:
                    if paramCode_param3 == '0':
                        valueC = inputs[inputs[i+3]]
                    elif paramCode_param3 == '1':
                        valueC = inputs[i+3]

        if opCode == '01':
            inputs[inputs[i+3]] = valueA+valueB
            i += 4
        elif opCode == '02':
            inputs[inputs[i+3]] = valueA*valueB
            i += 4
        elif opCode == '03':
            inputs[inputs[i+1]] = opCode3_input
            i += 2
        elif opCode == '04':
            returned_values.append(valueA)
            i += 2
        elif opCode == '05':
            if valueA != 0:
                i = valueB
            else:
                i += 3
        elif opCode == '06':
            if valueA == 0:
                i = valueB
            else:
                i += 3
        elif opCode == '07':
            if valueA < valueB:
                inputs[inputs[i+3]] = 1
            else:
                inputs[inputs[i+3]] = 0
            i += 4
        elif opCode == '08':
            if valueA == valueB:
                inputs[inputs[i+3]] = 1
            else:
                inputs[inputs[i+3]] = 0
            i += 4

    return inputs


def input_as_text(inputs):
    return ','.join((str(x) for x in inputs))


def test_walk_input():

    opCode3_input = 1
    r = walk_input([1, 0, 0, 0, 99], opCode3_input)
    r = input_as_text(r)
    assert r == '2,0,0,0,99'

    r = walk_input([2, 3, 0, 3, 99], opCode3_input)
    r = input_as_text(r)
    assert r == '2,3,0,6,99'

    r = walk_input([2, 4, 4, 5, 99, 0], opCode3_input)
    r = input_as_text(r)
    assert r == '2,4,4,5,99,9801'

    r = walk_input([1, 1, 1, 4, 99, 5, 6, 0, 99], opCode3_input)
    r = input_as_text(r)
    assert r == '30,1,1,4,2,5,6,0,99'

    inputs = get_input_from_file('./20191202.txt')
    inputs_parsed = convert_input(inputs[0])
    inputs_parsed[1] = 66
    inputs_parsed[2] = 35
    r = walk_input(inputs_parsed, opCode3_input)
    assert r[0] == 19690720

    r = walk_input([1002, 4, 3, 4, 33], opCode3_input)
    r = input_as_text(r)
    assert r == '1002,4,3,4,99'

    input_equal_8 = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
    r = walk_input(input_equal_8, 8)
    input_as_text(r)
    assert returned_values[-1] == 1

    r = walk_input(input_equal_8, 9)
    input_as_text(r)
    assert returned_values[-1] == 0

    input_less_than_8 = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
    r = walk_input(input_less_than_8, 6)
    input_as_text(r)
    assert returned_values[-1] == 1

    r = walk_input(input_less_than_8, 9)
    input_as_text(r)
    assert returned_values[-1] == 0

    r = walk_input([3, 3, 1108, -1, 8, 3, 4, 3, 99], 8)
    input_as_text(r)
    assert returned_values[-1] == 1

    r = walk_input([3, 3, 1108, -1, 8, 3, 4, 3, 99], 9)
    input_as_text(r)
    assert returned_values[-1] == 0

    r = walk_input([3, 3, 1107, -1, 8, 3, 4, 3, 99], 6)
    input_as_text(r)
    assert returned_values[-1] == 1

    r = walk_input([3, 3, 1107, -1, 8, 3, 4, 3, 99], 9)
    input_as_text(r)
    assert returned_values[-1] == 0

    r = walk_input([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], 8)
    input_as_text(r)
    assert returned_values[-1] == 1

    r = walk_input([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], 0)
    input_as_text(r)
    assert returned_values[-1] == 0

if __name__ == "__main__":
    # execute only if run as a script
    test_walk_input()
    # output = 0

    inputs = get_input_from_file('./20191205.txt')
    r = walk_input(convert_input(inputs[0]), 5)
    print(returned_values[-1])
