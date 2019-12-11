from itertools import permutations
from collections import defaultdict
import numpy as np


class RobotBrain:
    def __init__(self, program):
        self.program = program
        self.output = 0
        self.cursor = 0
        self.iteration = 0
        self.stop = False
        self.offset = 0


def get_input_from_file(file):
    with open(file, "r") as file_object:
        results = file_object.read().splitlines()
        return results


def convert_input(inputs):
    split_inputs = inputs.split(',')
    results = defaultdict(int)
    for i in range(len(split_inputs)):
        results[i] = int(split_inputs[i])
    return results


def run_pgm(amplifier, input):
    while amplifier.program[amplifier.cursor] != 99:
        instr = f"{amplifier.program[amplifier.cursor]:05}"
        opCode = instr[-2:]
        paramCode_param1 = instr[2]
        paramCode_param2 = instr[1]
        paramCode_param3 = instr[0]
        output_offset = 0
        if opCode in ['01', '02', '04', '05', '06', '07', '08', '09']:
            if paramCode_param1 == '0':
                valueA = amplifier.program[amplifier.program[amplifier.cursor+1]]
            elif paramCode_param1 == '1':
                valueA = amplifier.program[amplifier.cursor+1]
            elif paramCode_param1 == '2':
                valueA = amplifier.program[amplifier.program[amplifier.cursor+1]+amplifier.offset]

            if opCode in ['01', '02', '05', '06', '07', '08']:
                if paramCode_param2 == '0':
                    valueB = amplifier.program[amplifier.program[amplifier.cursor+2]]
                elif paramCode_param2 == '1':
                    valueB = amplifier.program[amplifier.cursor+2]
                elif paramCode_param2 == '2':
                    valueB = amplifier.program[amplifier.program[amplifier.cursor+2]+amplifier.offset]

                if opCode in []:
                    if paramCode_param3 == '0':
                        valueC = amplifier.program[amplifier.program[amplifier.cursor+3]]
                    elif paramCode_param3 == '1':
                        valueC = amplifier.program[amplifier.cursor+3]
                    if paramCode_param3 == '2':
                        output_offset = amplifier.offset

        if opCode in ['01', '02', '07', '08']:
            if paramCode_param3 == '2':
                output_offset = amplifier.offset

        if opCode in ['03']:
            if paramCode_param1 == '2':
                output_offset = amplifier.offset

        #print(instr, amplifier.offset, valueA, amplifier.cursor)

        if opCode == '01':
            amplifier.program[amplifier.program[amplifier.cursor+3]+output_offset] = valueA+valueB
            amplifier.cursor += 4
        elif opCode == '02':
            amplifier.program[amplifier.program[amplifier.cursor+3]+output_offset] = valueA*valueB
            amplifier.cursor += 4
        elif opCode == '03':
            # if amplifier.iteration == 0:
            #     val = phase
            # else:
            #     val = input
            amplifier.iteration += 1
            amplifier.program[amplifier.program[amplifier.cursor+1]+output_offset] = input
            amplifier.cursor += 2
        elif opCode == '04':
            amplifier.output = valueA
            # print(amplifier.output)
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
                amplifier.program[amplifier.program[amplifier.cursor+3]+output_offset] = 1
            else:
                amplifier.program[amplifier.program[amplifier.cursor+3]+output_offset] = 0
            amplifier.cursor += 4
        elif opCode == '08':
            if valueA == valueB:
                amplifier.program[amplifier.program[amplifier.cursor+3]+output_offset] = 1
            else:
                amplifier.program[amplifier.program[amplifier.cursor+3]+output_offset] = 0
            amplifier.cursor += 4
        elif opCode == '09':
            # print("instr : {0} - rel_base {1} - value {2}".format(instr, amplifier.offset, valueA))
            amplifier.offset += valueA
            #print("new offset {0}".format(offset))
            amplifier.cursor += 2
    amplifier.stop = True
    return amplifier


def input_as_text(inputs):
    return ','.join((str(x) for x in inputs))

 # def test_walk_input():
    # inputs = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
    # out = find_max_output(inputs, 0)
    # assert out == 139629729

    # inputs=[3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
    # out = find_max_output(inputs,0)
    # assert out == 18216

    # inputs=[3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
    # out = find_max_output(inputs,0)
    # assert out == 65210


if __name__ == "__main__":
    # execute only if run as a script
    # test_walk_input()
    # output = 0

    inputs = get_input_from_file('./20191211.txt')
    painting_grid = defaultdict(int)
    painted_list = defaultdict(int)
    max_x = 0
    max_y = 0
    min_x = 0
    min_y = 0
    pos = (0, 0)
    painting_grid[pos] = 1
    direction = 0
    intCodeProg = RobotBrain(convert_input(inputs[0]))
    while not intCodeProg.stop:
        intCodeProg = run_pgm(intCodeProg, painting_grid[pos])
        color = intCodeProg.output
        intCodeProg = run_pgm(intCodeProg, painting_grid[pos])
        turn = intCodeProg.output
        painting_grid[pos] = color
        painted_list[pos] = 1

        if turn == 0:
            direction = (direction - 1) % 4
        if turn == 1:
            direction = (direction + 1) % 4
        if direction == 0:
            pos = (pos[0], pos[1]+1)
        elif direction == 1:
            pos = (pos[0]+1, pos[1])
        elif direction == 2:
            pos = (pos[0], pos[1]-1)
        elif direction == 3:
            pos = (pos[0]-1, pos[1])
        # print(pos, color, turn, direction)

        max_x = max(pos[0], max_x)
        max_y = max(pos[1], max_y)
        min_x = min(pos[0], min_x)
        min_y = min(pos[1], min_y)

    for y in range(max_y, min_y-1, - 1):
        for x in range(min_x, max_x):
            if painting_grid[(x, y)] == 1:
                print("#", end="")
            else:
                print(" ", end="")
        print()
