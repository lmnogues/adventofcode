import common

def display(grid):
    print("#################")
    for line in grid:
        line_to_display="#"
        for value in line:
            if value=="X":
                line_to_display+=(f" X ")
            else:
                line_to_display+=(f"{value:2d} ")
        line_to_display+="#"
        print(line_to_display)
    print("#################")

def calculate_score(grid,number):
    display(grid)
    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            val=grid[y][x]
            if val=="X":
                pass
            else:
                total+= val
    
    print(total*number)
    return total*number

def play_game(grids,random_number,part2=False):
    for value in random_number:
        print(value)
        for grid in grids:
            tick_number(grid,value)
            # display(grid)
        if part2:
            victory= verify_grids_part2(grids,value)
            if victory!=0:
                return grids,value
        else:
            victory = verify_grids(grids,value)
            if victory!=0:
                return grids,value

def verify_grids(grids,number):
    for grid in grids:
        for y in range(len(grid)):
            col=list()
            for x in range(len(grid[y])):
                col.append(grid[y][x])
            if grid[y].count("X") == 5 or col.count("X")== 5 :
                print("victory!")
                return calculate_score(grid,number)  
    return 0

def verify_grids_part2(grids,number):
    grid_to_remove=set()
    
    for i,grid in enumerate(grids):
        for y in range(len(grid)):
            col=list()
            for x in range(len(grid[y])):
                col.append(grid[x][y])
            if grid[y].count("X") == 5 or col.count("X")== 5 :
                # print("victory!")
                grid_to_remove.add(i)

    if len(grid_to_remove) >0 :
        if len(grids)>1:  
            for g in sorted(grid_to_remove,reverse=True):
                display(grids[g])
                grids.pop(g)
        else:
            return calculate_score(grids[0],number)
    return 0

def tick_number(grid,value):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x]==value:
                grid[y][x]="X"    

def parse_grids(inputs):
    grids=list()
    current_grid=[]
    for input in inputs[2:]:
        print(input)
        if input !=b"":
            current_grid.append([int(x) for x in input.strip().replace(b"  ",b" ").split(b" ")])
        if len(current_grid)==5:
            grids.append(current_grid)
            current_grid=[]
    return grids
def validate_grid(grid,played_number):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            val=grid[y][x]
            if val in played_number[:79]:
                raise

def test():
    inputs=b"7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1\n\
\n\
22 13 17 11  0\n\
 8  2 23  4 24\n\
21  9 14 16  7\n\
 6 10  3 18  5\n\
 1 12 20 15 19\n\
\n\
 3 15  0  2 22\n\
 9 18 13 17  5\n\
19  8  7 25 23\n\
20 11 10 24  4\n\
14 21 16 12  6\n\
\n\
14 21 17 24  4\n\
10 16 15  9 19\n\
18  8 23 26 20\n\
22 11 13  6  5\n\
 2  0 12  3  7".splitlines()

    random_number=[int(x) for x in inputs[0].split(b",")]
    grid=parse_grids(inputs)
    print(random_number)
    [display(g) for g in grid]    
    play_game(grid,random_number,True)


def main():
    inputs=common.get_inputs_from_site(2021,4)
    random_number=[int(x) for x in inputs[0].split(b",")]
    grid=parse_grids(inputs)
    print(random_number)
    [display(g) for g in grid]    
    final_grid,value = play_game(grid,random_number,True)
    display(final_grid[0])
    print(value)
    validate_grid(final_grid[0],random_number)


# test()
main()