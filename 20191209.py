

from collections import defaultdict


def get_input_from_file(file):
    with open(file, "r") as file_object:
        results = file_object.read().splitlines()
        return results


def convert_input(inputs):
    split_inputs = inputs.split(',')
    results = defaultdict()
    for i in range(len(split_inputs)):
        results[i] = int(split_inputs[i])
    return results


returned_values = list()


def walk_input(inputs, opCode3_input):
    i = 0
    returned_values.clear()
    offset = 0

    while inputs[i] != 99:
        instr = f"{inputs[i]:05}"
        opCode = instr[-2:]
        valueA = ""
        valueB = ""
        paramCode_param1 = instr[2]
        paramCode_param2 = instr[1]
        paramCode_param3 = instr[0]
        output_offset = 0
        if opCode in ['01', '02', '04', '05', '06', '07', '08', '09']:
            if paramCode_param1 == '0':
                valueA = inputs[inputs[i+1]]
            elif paramCode_param1 == '1':
                valueA = inputs[i+1]
            elif paramCode_param1 == '2':
                valueA = inputs[inputs[i+1]+offset]

            if opCode in ['01', '02', '05', '06', '07', '08']:
                if paramCode_param2 == '0':
                    valueB = inputs[inputs[i+2]]
                elif paramCode_param2 == '1':
                    valueB = inputs[i+2]
                elif paramCode_param2 == '2':
                    valueB = inputs[inputs[i+2]+offset]

                if opCode in []:
                    if paramCode_param3 == '2':
                        output_offset = offset

        if opCode in ['01', '02', '07', '08']:
            if paramCode_param3 == '2':
                output_offset = offset

        if opCode in ['03']:
            if paramCode_param1 == '2':
                output_offset = offset

        #print(i, int(instr), valueA, valueB, offset)

        if opCode == '01':
            inputs[inputs[i+3]+output_offset] = valueA+valueB
            #print("writing {0} in position {1}".format(valueA+valueB, inputs[i+3]+output_offset))
            i += 4
        elif opCode == '02':
            inputs[inputs[i+3]+output_offset] = valueA*valueB
            #print("writing {0} in position {1}".format(valueA*valueB, inputs[i+3]+output_offset))
            i += 4
        elif opCode == '03':
            inputs[inputs[i+1]+output_offset] = opCode3_input
            #print("writing {0} in position {1}".format(opCode3_input, inputs[i+1]+output_offset))
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
                inputs[inputs[i+3]+output_offset] = 1
                #print("writing {0} in position {1}".format(1, inputs[i+3]+output_offset))
            else:
                inputs[inputs[i+3]+output_offset] = 0
                #print("writing {0} in position {1}".format(0, inputs[i+3]+output_offset))
            i += 4
        elif opCode == '08':
            if valueA == valueB:
                inputs[inputs[i+3]+output_offset] = 1
                #print("writing {0} in position {1}".format(1, inputs[i+3]+output_offset))
            else:
                inputs[inputs[i+3]+output_offset] = 0
                #print("writing {0} in position {1}".format(1, inputs[i+3]+output_offset))
            i += 4
        elif opCode == '09':
            ##print("instr : {0} - rel_base {1} - value {2}".format(instr, offset, valueA))
            offset += valueA
            #print("new offset {0}".format(offset))
            i += 2

    return inputs


def input_as_text(inputs):
    return ','.join((str(x) for x in inputs))


def test_walk_input():

    r = walk_input([104, 1125899906842624, 99], 0)
    assert returned_values[0] == 1125899906842624
    returned_values.clear()


if __name__ == "__main__":
    # execute only if run as a script
  #  test_walk_input()
    # output = 0

    inputs = get_input_from_file('./20191209.txt')
    r = walk_input(convert_input(inputs[0]), 2)
    print(returned_values)
