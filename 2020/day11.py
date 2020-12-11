import common
import copy
from collections import Counter
from matplotlib import pyplot as plt
from celluloid import Camera

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

def plot_display_seats(seats,camera,axe):    
    colored_data=copy.deepcopy(seats)
    for r in range(len(colored_data)):
        row=colored_data[r]
        for c in range(len(row)):
            if row[c]=="L":
                colored_data[r][c]=(255,255,255)
            elif row[c]=="#":
                colored_data[r][c]=(123,200,50)
            else :
                colored_data[r][c]=(0,0,0)
    axe.imshow(colored_data, interpolation='nearest')
    camera.snap()
    

def process_inputs(inputs,nb_seats=4,part=1,camera=None,axe=None):
    seats = [list(y) for y in [x for x in inputs]]
    changed=True    
    frame=True
    while changed:                
        changed,seats = occupied_seats(seats,nb_seats,part)
        if frame:
            plot_display_seats(seats,camera,axe)   
        frame=not frame
    plot_display_seats(seats,camera,axe)  
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

    fig, axes  = plt.subplots(2)
    camera = Camera(fig)
    counter = process_inputs(inputs.splitlines(),camera=camera,axe=axes[0])
    assert 37 == counter["#"]     
    counter = process_inputs(inputs.splitlines(),5,2,camera,axe=axes[1])
    assert 26 == counter["#"] 
    anim = camera.animate()
    plt.show()
    

def main():
    inputs=common.get_input_from_file("day11.txt")
    
    fig, axes  = plt.subplots(2)
    camera = Camera(fig)
    counter = process_inputs(inputs,camera=camera,axe=axes[0])
    assert 2273 == counter["#"]
    counter = process_inputs(inputs,5,2,camera,axes[1])
    print(counter["#"])
    anim = camera.animate()
    plt.show()

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
