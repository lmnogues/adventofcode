import numpy
import common

def transform_terrain_to_array(inputs):
    return numpy.vstack([numpy.array(list(line)) for line in inputs])
        
def slide_the_terrain(terrain,movement,start_pos):
    y_size=terrain.shape[0]
    x_size=terrain.shape[1]
    current_pos=start_pos
    tree_met=0
    while current_pos[0]< y_size:
        # print(f"current position is {current_pos} - terrain value is [{terrain[current_pos]}] - tree met so far : {tree_met}")
        if terrain[current_pos]=="#":
            tree_met+=1
        y_pos=current_pos[0]+movement[0]
        x_pos=current_pos[1]+movement[1]
        x_pos%=x_size

        current_pos=(y_pos,x_pos)
            
    return tree_met

def test():
    inputs=["..##.......",
            "#...#...#..",
            ".#....#..#.",
            "..#.#...#.#",
            ".#...##..#.",
            "..#.##.....",
            ".#.#.#....#",
            ".#........#",
            "#.##...#...",
            "#...##....#",
            ".#..#...#.#"]
    terrain = transform_terrain_to_array(inputs)
    starting_pos=(0,0)
    tree_met = slide_the_terrain(terrain,(1,3),starting_pos)
    assert tree_met==7
    list_of_slopes=[(1,1),(1,3),(1,5),(1,7),(2,1)]
    result=1
    for slopes in list_of_slopes:
        result=result*slide_the_terrain(terrain,slopes,starting_pos)
    assert result==336


def main():
    inputs=common.get_input_from_file("day3.txt")
    
    lines = [x.strip() for x in inputs]

    terrain=transform_terrain_to_array(inputs)
    starting_pos=(0,0)

    tree_met = slide_the_terrain(terrain,(1,3),starting_pos)  
    print(f"part_1 : {tree_met=}")
    assert tree_met==282
    list_of_slopes=[(1,1),(1,3),(1,5),(1,7),(2,1)]
    result=1
    for slopes in list_of_slopes:
        result=result*slide_the_terrain(terrain,slopes,starting_pos)
    
    print(f"part_2 : {result=}")
    assert result==958815792

test()
main()