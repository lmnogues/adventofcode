import common
import copy

class instruction:
    def __init__(self,value):
        instr=value.split()
        self.instr=instr[0]
        self.value=int(instr[1])

    def __str__(self) -> str:
        return f"{self.instr=} {self.value=}"

    def __repr__(self) -> str:
        return self.__str__()

def run_instructions(instructions,input_value=0):
    index=0
    known_index=[]
    while index not in known_index:
        prev_index=index
        known_index.append(index)
        instr=instructions[index]
        #print(f"current instruction {instr} => {input_value =}")
        if instr.instr in "nop":
            index+=1
        elif instr.instr in "acc":
            index+=1
            input_value+=instr.value
        elif instr.instr in "jmp":
            index+=instr.value
        else:
            print("Unkwnon command")
            return -1,input_value        
        
        if  prev_index == len(instructions)-1:
            return 0,input_value

    return -1,input_value

def find_all_possible_corruption(instructions):
    possibilities=[instructions]
    for i in instructions:
        if i.instr in "nop":
            new_possibility= copy.deepcopy(instructions)
            idx=instructions.index(i)
            new_possibility[idx].instr="jmp"
            possibilities.append(new_possibility)
        elif i.instr in "jmp":
            new_possibility= copy.deepcopy(instructions)
            idx=instructions.index(i)
            new_possibility[idx].instr="nop"
            possibilities.append(new_possibility)
    return possibilities
def test():
    inputs="""nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
    instructions=[instruction(i) for i in inputs.splitlines()]
    possibilities=find_all_possible_corruption(instructions)
    print(len(possibilities))

    assert -1,5 == run_instructions(instructions)

    results=[run_instructions(p) for p in possibilities]
    assert [8] == [r[1] for r in results if r[0]==0]

def main():
    inputs=common.get_input_from_file("day8.txt")
    instructions=[instruction(i) for i in inputs]
    
    assert -1,1949 == run_instructions(instructions)

    possibilities=find_all_possible_corruption(instructions)
    print(len(possibilities))
    
    results=[run_instructions(p) for p in possibilities]
    print([r[1] for r in results if r[0]==0])

test()
main()