from itertools import permutations

class Amplifier:
    def __init__(self, program):
        self.program = program.copy()
        self.output=0
        self.cursor=0
        self.iteration=0
        self.stop=False



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


def run_pgm(amplifier, phase,input):
    while amplifier.program[amplifier.cursor] != 99:
        instr = f"{amplifier.program[amplifier.cursor]:05}"
        opCode = instr[-2:]
        paramCode_param1 = instr[2]
        paramCode_param2 = instr[1]
        paramCode_param3 = instr[0]

        if opCode in ['01', '02', '04', '05', '06', '07', '08']:
            if paramCode_param1 == '0':
                valueA = amplifier.program[amplifier.program[amplifier.cursor+1]]
            elif paramCode_param1 == '1':
                valueA = amplifier.program[amplifier.cursor+1]

            if opCode in ['01', '02', '05', '06', '07', '08']:
                if paramCode_param2 == '0':
                    valueB = amplifier.program[amplifier.program[amplifier.cursor+2]]
                elif paramCode_param2 == '1':
                    valueB = amplifier.program[amplifier.cursor+2]

                if opCode in []:
                    if paramCode_param3 == '0':
                        valueC = amplifier.program[amplifier.program[amplifier.cursor+3]]
                    elif paramCode_param3 == '1':
                        valueC = amplifier.program[amplifier.cursor+3]

        if opCode == '01':
            amplifier.program[amplifier.program[amplifier.cursor+3]] = valueA+valueB
            amplifier.cursor += 4
        elif opCode == '02':
            amplifier.program[amplifier.program[amplifier.cursor+3]] = valueA*valueB
            amplifier.cursor += 4
        elif opCode == '03':
            if amplifier.iteration == 0:
                val = phase
            else:
                val = input
            amplifier.iteration+=1
            amplifier.program[amplifier.program[amplifier.cursor+1]] = val
            amplifier.cursor += 2
        elif opCode == '04':
            amplifier.output = valueA
            amplifier.cursor += 2
            return amplifier
        elif opCode == '05':
            if valueA != 0:
                amplifier.cursor = valueB
            else:
                amplifier.cursor += 3
        elif opCode == '06':
            if valueA == 0:
                amplifier.cursor = valueB
            else:
                amplifier.cursor += 3
        elif opCode == '07':
            if valueA < valueB:
                amplifier.program[amplifier.program[amplifier.cursor+3]] = 1
            else:
                amplifier.program[amplifier.program[amplifier.cursor+3]] = 0
            amplifier.cursor += 4
        elif opCode == '08':
            if valueA == valueB:
                amplifier.program[amplifier.program[amplifier.cursor+3]] = 1
            else:
                amplifier.program[amplifier.program[amplifier.cursor+3]] = 0
            amplifier.cursor += 4
    amplifier.stop = True
    return amplifier


def calculate_all_possible_output(inputs, provided_input):
    phase_results = {}
    phases = permutations(range(5, 10), 5)
    for phase in phases:
        amps=[Amplifier(inputs) for step in range(5)]
        
        while not amps[4].stop:
            for i in range(5):
                amps[i]=run_pgm(amps[i],phase[i],amps[i-1].output)
                phase_results[phase]=amps[i].output
    return phase_results

def find_max_output(inputs, provided_input):
    phase_results = calculate_all_possible_output(inputs,provided_input)
    max_value = max([res for res in phase_results.values()])
    return max_value


def input_as_text(inputs):
    return ','.join((str(x) for x in inputs))


def test_walk_input():
    inputs = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
    out = find_max_output(inputs, 0)
    assert out == 139629729

    inputs=[3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
    out = find_max_output(inputs,0)
    assert out == 18216

    # inputs=[3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
    # out = find_max_output(inputs,0)
    # assert out == 65210


if __name__ == "__main__":
    # execute only if run as a script
    test_walk_input()
    # output = 0

    inputs = get_input_from_file('./20191207.txt')
    r = find_max_output(convert_input(inputs[0]), 0)
    print(r)
