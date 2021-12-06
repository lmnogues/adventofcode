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
    for input in inputs:
        if input[0][0]==input[1][0] or input[0][1]==input[1][1]:
            result.append(input)
    return result

def cover_ground(inputs):
    result=numpy.zeros((2,2))
    print(result)
    for input in inputs:
        x1=x2=y1=y2=-1
        if input[0][0]<=input[1][0]:
            x1=input[0][0]
            x2=input[1][0]
        else:
            x2=input[0][0]
            x1=input[1][0]
        
        if input[0][1]<=input[1][1]:
            y1=input[0][1]
            y2=input[1][1]
        else:
            y2=input[0][1]
            y1=input[1][1]
        print(x1,x2,y1,y2)
        if x1==x2:            
            for y in range(y1,y2):
                if result[x1] is None:
                    result[x1]=[]
                if result[x1][y] is None:
                    result[x1][y]=1
                else:
                    result[x1][y]+=1
        if y1==y2:
            for x in range(x1,x2):
                if result[x] is None:
                    result[x]=[]
                if result[x][y1] is None:
                    result[x][y1]=1
                else:
                    result[x][y1]+=1

    print(result)

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
    inputs=filter_part1(inputs)
    cover_ground(inputs)

test()
