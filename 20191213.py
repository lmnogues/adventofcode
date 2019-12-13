from itertools import permutations
from collections import defaultdict
import numpy as np
import random


class ArcadeCabinet:
    def __init__(self, program):
        self.program = program
        self.output = 0
        self.output_list = list()
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
            amplifier.program[amplifier.program[amplifier.cursor+1]+output_offset] = input
            amplifier.cursor += 2
            return amplifier
        elif opCode == '04':
            amplifier.output_list.append(valueA)
            amplifier.output = valueA
            amplifier.cursor += 2
            if len(amplifier.output_list) == 3:
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


CHARS = {
    0: " ",
    1: "#",
    2: "@",
    3: "_",
    4: "O",
}

if __name__ == "__main__":
    # execute only if run as a script
    # test_walk_input()
    # output = 0

    inputs = get_input_from_file('./20191213.txt')
    intCodeProg = ArcadeCabinet(convert_input(inputs[0]))
    nb_block = 0
    score = 0
    input = 0
    intCodeProg.program[0] = 2
    tile_list = list()
    ball_xpos = 0
    paddle_xpos = 0
    move_once = False
    screen = defaultdict()
    while not intCodeProg.stop:
        intCodeProg = run_pgm(intCodeProg, input)
        if len(intCodeProg.output_list) == 3:
            x_pos, y_pos, tile_id = intCodeProg.output_list
            intCodeProg.output_list.clear()

            if tile_id == 2:
                nb_block += 1
            if x_pos == -1 and y_pos == 0:
                score = tile_id
            else:
                screen[(y_pos, x_pos)] = tile_id
            input = 0
            if tile_id == 4 and move_once:
                ball_xpos = x_pos

                if ball_xpos > paddle_xpos:
                    input = +1
                if ball_xpos < paddle_xpos:
                    input = -1

                move_once = False
            elif tile_id == 3 and not move_once:
                paddle_xpos = x_pos
                move_once = True

        # if tile_id == 3 or tile_id == 4:

    prev_y = 0
    print("SCREEN : ")
    for y, x in sorted(screen.keys()):
        if prev_y != y:
            print()
        print(CHARS[screen[(y, x)]], end="")
        prev_y = y
    print("")

    print("NB_BLOCK : ", nb_block)
    print(score)
