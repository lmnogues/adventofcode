import common
from numpy import *


def move_to_pos_part1(inputs,pos):    
    cost=0
    for val in inputs:
        cost+=abs(val - pos)
    return cost

def move_to_pos_part2(inputs,pos):
    
    cost=0
    for val in inputs:
        dist=abs(val - pos)
        cost+=int(dist*(dist+1)/2)
    return cost

def analyse_cost(inputs):
    result={}
    for i in range(max(inputs)):
        result[i] = move_to_pos_part1(inputs,i)
    
    print("part1",min(result.items(), key=lambda x: x[1]) )
    
    result={}
    for i in range(max(inputs)):
        result[i] = move_to_pos_part2(inputs,i)
    
    print("part2",min(result.items(), key=lambda x: x[1]) )

def test():
    inputs=[int(x) for x in "16,1,2,0,4,2,7,1,2,14".split(",")]        
    analyse_cost(inputs)

def main():
    inputs=common.get_integer_inputs(year=2021,day=7,split=",")
    analyse_cost(inputs)


test()
main()