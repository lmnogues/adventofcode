from enum import Enum
import common
import math

def rotate_origin(xy, deg):
    """Only rotate a point around the origin (0, 0)."""
    x, y = xy
    rad=deg*(math.pi/180)
    xx = x * math.cos(rad) + y * math.sin(rad)
    yy = -x * math.sin(rad) + y * math.cos(rad)

    return xx, yy
    
class Direction(Enum):
    NORTH=0
    EAST=90
    SOUTH=180
    WEST=270

def drive_the_ferry(inputs,direction:Direction,position=(0,0)):
    current_direction=direction
    for instr in inputs:
        if instr[0]=="F":
            if current_direction == Direction.NORTH:
                position=(position[0]),position[1]+int(instr[1:])            
            elif current_direction == Direction.SOUTH:
                position=(position[0]),position[1]-int(instr[1:])            
            elif current_direction == Direction.EAST:
                position=(position[0]+int(instr[1:]),position[1])
            elif current_direction == Direction.WEST:
                position=(position[0]-int(instr[1:]),position[1])            
        elif instr[0]=="N":
            position=(position[0]),position[1]+int(instr[1:])   
        elif instr[0]=="S":
            position=(position[0]),position[1]-int(instr[1:])   
        elif instr[0]=="E":
            position=(position[0]+int(instr[1:]),position[1])   
        elif instr[0]=="W":
            position=(position[0]-int(instr[1:]),position[1])   
        elif instr[0]=="R":
            current_direction=Direction((current_direction.value+int(instr[1:]))%360)
        elif instr[0]=="L":
            current_direction=Direction((current_direction.value-int(instr[1:]))%360)
        else :
            print("unknown instr")
            break
        #print(f"{instr=} {position=} {current_direction=}")
    return abs(position[0])+abs(position[1])
    
def drive_the_waipoint(inputs,direction:Direction,boat_pos=(0,0),wp_pos=(0,0)):
    for instr in inputs:
        if instr[0]=="F":
            for i in range(int(instr[1:])):
                boat_pos=(boat_pos[0]+wp_pos[0],boat_pos[1]+wp_pos[1])            
        elif instr[0]=="N":
            wp_pos=(wp_pos[0]),wp_pos[1]+int(instr[1:])   
        elif instr[0]=="S":
            wp_pos=(wp_pos[0]),wp_pos[1]-int(instr[1:])   
        elif instr[0]=="E":
            wp_pos=(wp_pos[0]+int(instr[1:]),wp_pos[1])   
        elif instr[0]=="W":
            wp_pos=(wp_pos[0]-int(instr[1:]),wp_pos[1])   
        elif instr[0]=="R":
            wp_pos=rotate_origin(wp_pos,int(instr[1:]))
        elif instr[0]=="L":
            wp_pos=rotate_origin(wp_pos,-1*int(instr[1:]))
        else :
            print("unknown instr")
            break
        # print(f"{instr=} {boat_pos=} {wp_pos=}")
    return abs(boat_pos[0])+abs(boat_pos[1])
    
def test():
    inputs="""F10
N3
F7
R90
F11"""
    inputs=inputs.splitlines()
    assert 25 == drive_the_ferry(inputs,Direction.EAST)
    assert 286 == drive_the_waipoint(inputs,Direction.EAST,(0,0),(10,1))


def main():
    inputs=common.get_data_from_file("day12.txt").splitlines()
    print(drive_the_ferry(inputs,Direction.EAST))
    print(drive_the_waipoint(inputs,Direction.EAST,(0,0),(10,1)))

test()
main()
