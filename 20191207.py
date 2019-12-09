from itertools import permutations


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


def walk_input(inputs, opCode3_input, phase):
    i = 0
    is_first_input = True
    returned_value = opCode3_input
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
            if is_first_input:
                val = phase
                is_first_input = False
            else:
                val = returned_value
            inputs[inputs[i+1]] = val
            i += 2
        elif opCode == '04':
            returned_value = valueA
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
    return returned_value

def calculate_all_possible_output(inputs,provided_input):
    phase_results={}
    for phase in permutations(range(5),5):
        input_code=provided_input
        for step in phase:
            input_code=walk_input(inputs.copy(),input_code,step)          
        phase_results[phase] = input_code  
    return phase_results

def find_max_output(inputs,provided_input):
    phase_results =calculate_all_possible_output(inputs,provided_input)
    max_value = max([res for res in phase_results.values()])
    return max_value

def input_as_text(inputs):
    return ','.join((str(x) for x in inputs))


def test_walk_input():
    inputs=[3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
    out = find_max_output(inputs,0)
    assert out == 43210
    
    inputs=[3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
    out = find_max_output(inputs,0)
    assert out == 54321

    inputs=[3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
    out = find_max_output(inputs,0)
    assert out == 65210

if __name__ == "__main__":
    # execute only if run as a script
    test_walk_input()
    # output = 0

    inputs = get_input_from_file('./20191207.txt')
    r = find_max_output(convert_input(inputs[0]), 0)
    print(r)
