import common
import time

def calculate_next_bus_part1(time,buses):
    next_schedule= None
    for b in buses:        
        new_time=(int(time/b)+1)*b
        if next_schedule is None:
            next_schedule=b,new_time
        else:
            if next_schedule[1] > new_time:
                next_schedule=b,new_time
    calculation = (next_schedule[1]-time)*next_schedule[0]
    return calculation


    
def is_valid_time(next_time,time,buses,max_b):
    for i,b in enumerate(buses):
        if b!="x":
            b=int(b)
            if b!=max_b:
                b_next=(((int((time)/b)+1)*b)-i)
                while b_next > time:
                    b_next=b_next-b
                if time!=b_next:
                    return False
    return True
                


def calculate_next_common_schedule_part2(time,buses):
    next_schedule= None
    max_b=max([int(x) for x in buses if x!="x"])
    print(max_b)
    offset=buses.index(str(max_b))
    jump=max_b
    while True:        
        next_time=(int((time)/max_b)+1)*max_b
        time=(next_time-offset)+max_b
        all=is_valid_time(next_time,time,buses,max_b)
        if all:
            print(f"Found time : {time}")
            break
    return time

def solve_2(buses):
    data = [(i, int(bus_id)) for i, bus_id in enumerate(buses) if bus_id != 'x']   
    jump = data[0][1]
    print(f"starting with {data} {jump}")
    time_stamp = 0
    for delta, bus_id in data[1:]:
        while (time_stamp + delta) % bus_id != 0:
            time_stamp += jump
        jump *= bus_id
    print(f"result is {time_stamp}")
    return time_stamp

def parse_inputs_part1(inputs):
    time=int(inputs[0])
    buses=[int(y) for y in inputs[1].split(",") if y!="x"]
    return time,buses
  
def parse_inputs_part2(inputs):
    time=int(inputs[0])
    buses=[y for y in inputs[1].split(",")]
    return time,buses      
def test():
    inputs="""939
7,13,x,x,59,x,31,19"""
    time,buses=parse_inputs_part1(inputs.splitlines())
    assert 295 ==calculate_next_bus_part1(time,buses)

def test2():
    inputs="""939
17,x,13,19"""    
    time,buses=parse_inputs_part2(inputs.splitlines())
    assert 3417 == calculate_next_common_schedule_part2(time,buses)
    solve_2(buses)
    
    inputs="""750018
67,7,59,61"""    
    time,buses=parse_inputs_part2(inputs.splitlines())
    assert 754018==  calculate_next_common_schedule_part2(time,buses)
    
    inputs="""770010
67,x,7,59,61"""    
    time,buses=parse_inputs_part2(inputs.splitlines())
    assert 779210==  calculate_next_common_schedule_part2(time,buses)
        
    inputs="""1201476
67,7,x,59,61"""    
    time,buses=parse_inputs_part2(inputs.splitlines())
    assert 1261476 == calculate_next_common_schedule_part2(time,buses)
    
    inputs="""1202101486
1789,37,47,1889"""    
    time,buses=parse_inputs_part2(inputs.splitlines())
    assert 1202161486 == calculate_next_common_schedule_part2(time,buses)
    
def main():
    inputs=common.get_input_from_file("day13.txt")
    tt,buses=parse_inputs_part1(inputs)
    part1=calculate_next_bus_part1(tt,buses)
    print(part1)
    
    tt,buses=parse_inputs_part2(inputs)
    
    assert 210612924879242 == solve_2(buses)

test()
test2()
main()
