import math
import common
import re
import numpy

def parse_inputs(inputs):
    result=[]
    for line in inputs:
        x_start,y_start,x_end,y_end = re.split(",| -> ",line)
        result.append([(int(x_start),int(y_start)),(int(x_end),int(y_end))])
    return result

def filter_part1(inputs):
    result=[]
    max_x=max_y=0
    for input in inputs:
        if input[0][0]==input[1][0] or input[0][1]==input[1][1]:
            result.append(input)
        if max_x < input[0][0] or max_x < input[1][0]:
            max_x = max(input[0][0],input[1][0])
        if max_y < input[0][1] or max_y < input[1][1]:
            max_y=max(input[0][1],input[1][1])

    return result,(max_x+1,max_y+1)

def cover_ground(inputs,dimension):
    result=numpy.zeros(dimension,dtype=int)
    #print(result)
    for input in inputs:
        x1=input[0][0]
        x2=input[1][0]
        y1=input[0][1]
        y2=input[1][1]   

        dx = x2-x1
        dy = y2-y1
        i_range=range(1+max(abs(dx),abs(dy)))
        print(i_range)
        
        if dx>0:
            next_x=1
        else:
            if dx<0:
                next_x=-1
            else:
                next_x=0
        if dy>0:
            next_y=1
        else:
            if dy<0:
                next_y=-1
            else:
                next_y=0
        for i in i_range:
            x = x1+next_x*i
            y = y1+next_y*i
            result[y][x] += 1

    print(result)
    print(len(result[result >=2]))

def test():
    inputs=b"0,9 -> 5,9\n\
8,0 -> 0,8\n\
9,4 -> 3,4\n\
2,2 -> 2,1\n\
7,0 -> 7,4\n\
6,4 -> 2,0\n\
0,9 -> 2,9\n\
3,4 -> 1,4\n\
0,0 -> 8,8\n\
5,5 -> 8,2".decode('UTF-8').splitlines()
    inputs = parse_inputs(inputs)
    print(inputs)
    filtered_inputs,dimension=filter_part1(inputs)
    # cover_ground(filtered_inputs,dimension)
    cover_ground(inputs,dimension)

def main():
    inputs = common.get_inputs_from_site(2021,5)
    inputs = parse_inputs(inputs)
    print(inputs)
    finputs,dimension=filter_part1(inputs)
    # cover_ground(finputs,dimension)
    cover_ground(inputs,dimension)

test()
main()