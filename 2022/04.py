import common

test_inputs="""2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

test_lines=test_inputs.split("\n")

def part1(lines):
    count=0
    for line in lines:
        ranges=[(int(x[0]),int(x[1])) for x in [l.split("-") for l in line.split(",")]]
        x1=ranges[0][0]
        y1=ranges[0][1]
        x2=ranges[1][0]
        y2=ranges[1][1]

        if x1 <= x2 and y2 <= y1:
            #intersect
            # print(line,"x1 <= x2 and y2 <= y1")
            count+=1
        elif x2 <= x1 and y1 <= y2:
            #intersect
            # print(line,"x2 <= x1 and y1 <= y2")
            count+=1
        
        
    print(count)
    

def part2(lines):
    count=0
    notOverlappingPairs=0
    for line in lines:
        ranges=[(int(x[0]),int(x[1])) for x in [l.split("-") for l in line.split(",")]]
        x1=ranges[0][0]
        y1=ranges[0][1]
        x2=ranges[1][0]
        y2=ranges[1][1]

        if  x1 < x2 and y1 < x2  :
            #intersect
            # print(line,"x1 <= x2 and y2 <= y1")
            count+=1
            
        elif x2 < x1 and y2 < x1:
            #intersect
            # print(line,"x2 <= x1 and y1 <= y2")
            count+=1

    print(len(lines)-count)
    


part1(test_lines)
part2(test_lines)

file_input=common.get_data_from_file("2022/04.txt")
part1(file_input.split("\n"))
part2(file_input.split("\n"))
    
