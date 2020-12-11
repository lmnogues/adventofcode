import common
import numpy
import copy
from collections import Counter


def check_availability(x,y,seats,part):
    list_seats=[]
    if part==1:
        for x_pos in range(x-1,x+2):
            if 0<= x_pos  < len(seats):
                for y_pos in range(y-1,y+2):
                    if 0<= y_pos < len(seats[0]):
                        if y_pos!=y or x_pos!=x:
                            list_seats.append(seats[x_pos][y_pos])
    else:
        for x_pos in [-1,0,1]:
            for y_pos in [-1,0,1]:
                if not (x_pos==0 and y_pos==0):
                    xx=x+x_pos
                    yy=y+y_pos
                    while 0<= xx  < len(seats) and 0<= yy < len(seats[0]) and seats[xx][yy]==".":
                        xx=xx+x_pos
                        yy=yy+y_pos
                    if  0<= xx  < len(seats) and 0<= yy < len(seats[0]):
                        list_seats.append(seats[xx][yy])
        
    return len([x for x in list_seats if x=="#"])

            
def occupied_seats(seats,nb_seat=4,part=1):
    changed=False
    seat_results=copy.deepcopy(seats)
    for x in range(len(seats)):
        line=seats[x]
        for y in range(len(line)):
            col=line[y]
            if col == "L":
                if check_availability(x,y,seats,part)==0:
                    seat_results[x][y]="#"
                    changed=True
            if col == "#":
                if check_availability(x,y,seats,part)>=nb_seat:                    
                    seat_results[x][y]="L"
                    changed=True
    
    return changed,seat_results

def display_seats(seats):
    for line in seats:
        print("".join(line))
    print("-"*len(seats[0]))

def count_seats(seats):
    counter=Counter()
    [counter.update(x) for x in seats]
    print(counter)
    return counter

def process_inputs(inputs,nb_seats=4,part=1):
    seats = [list(y) for y in [x for x in inputs]]
    # display_seats(seats)
    changed=True
    while changed:        
        changed,seats = occupied_seats(seats,nb_seats,part)
        # display_seats(seats)   
    counter=count_seats(seats)
    return counter

def test():
    inputs="""L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
    counter = process_inputs(inputs.splitlines())
    assert 37 == counter["#"] 
    counter = process_inputs(inputs.splitlines(),5,2)
    assert 26 == counter["#"] 

def main():
    inputs=common.get_input_from_file("day11.txt")
    counter = process_inputs(inputs)
    assert 2273 == counter["#"]
    counter = process_inputs(inputs,5,2)
    print(counter["#"])

def test2():
    inputs=""".......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#....."""
    seats = [list(y) for y in [x for x in inputs.splitlines()]]
    print(seats[4][3])
    assert 8 == check_availability(4,3,seats,2)

test()
test2()
main()
