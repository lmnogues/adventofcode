import common
import re
#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

stacks=[['N',"Z"],["D","C","M"],["P"]]

instructions_test="""move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

def parse_instruction(instructions_test):
    instructions=list()
    for line in instructions_test.split("\n"):
        all=re.search(r"move (\d+) from (\d+) to (\d+)",line)
        instructions.append(all.groups())
    return instructions

def work_the_crane_9000(stacks,instructions):
    print(stacks)
    for inst in instructions:
        
        #print(inst)
        start_pos=int(inst[1])-1
        end_pos=int(inst[2])-1
        qty=int(inst[0])
        for q in range(qty):
            s=stacks[start_pos][0]
            stacks[start_pos].remove(s)
            stacks[end_pos].insert(0,s)
            #print(stacks)
    for s in stacks:
        print(s[0],end="")
    print()

def work_the_crane_9001(stacks,instructions):
    print(stacks)
    for inst in instructions:
        
        print(inst)
        start_pos=int(inst[1])-1
        end_pos=int(inst[2])-1
        qty=int(inst[0])
        s=stacks[start_pos][0:qty]
        s.reverse()
        for r in s:
            stacks[start_pos].remove(r)
            stacks[end_pos].insert(0,r)
        print(stacks)
    for s in stacks:
        print(s[0],end="")
    print()

instructions=parse_instruction(instructions_test)
# work_the_crane_9000(stacks,instructions)

work_the_crane_9001(stacks,instructions)


stacks="""TVJWNRMS
VCPQJDWB
PRDHFJB
DNMBPRF
BTPRVH
TPBC
LPRJB
WBZTLSCN
GSL"""
def parse_stacks(stacks):
    results=list()
    for s in stacks.split("\n"):
        stack=list()
        for crane in s:
            stack.append(crane)
        results.append(stack)
    return results

file_input=common.get_data_from_file("2022/05.txt")
instructions=parse_instruction(file_input)
work_the_crane_9001(parse_stacks(stacks),instructions)

# [T] [V]                     [W]    
# [V] [C] [P] [D]             [B]    
# [J] [P] [R] [N] [B]         [Z]    
# [W] [Q] [D] [M] [T]     [L] [T]    
# [N] [J] [H] [B] [P] [T] [P] [L]    
# [R] [D] [F] [P] [R] [P] [R] [S] [G]
# [M] [W] [J] [R] [V] [B] [J] [C] [S]
# [S] [B] [B] [F] [H] [C] [B] [N] [L]
#  1   2   3   4   5   6   7   8   9 
