import common


def walk_the_plane(code):
    start=0
    end=127
    row_start=0
    row_end=7
    for letter in code:
        position_calculation=int((end-start)/2)
        row_calculation=int((row_end-row_start)/2)
        if letter=="B":
            start=start+position_calculation+1
        if letter=="F":
            end=end-position_calculation-1
        if letter=="R":
            row_start=row_start+row_calculation+1
        if letter=="L":
            row_end=row_end-row_calculation-1
    result=start*8+row_start
    return result

def find_missing_seat(seats):
    seats.sort()
    for s in range(len(seats)):
        if seats[s+1] - seats[s] ==2:
            return seats[s]+1

def test():
    input="FBFBBFFRLR"
    assert 357 == walk_the_plane(input)
    
    input="BFFFBBFRRR"
    assert 567 == walk_the_plane(input)
    
    input="FFFBBBFRRR"
    assert 119 == walk_the_plane(input)

    input="BBFFBBFRLL"
    assert 820 == walk_the_plane(input)

def main():
    inputs=common.get_input_from_file("day5.txt")
    all_occupied=list()
    for i in inputs:
        all_occupied.append(walk_the_plane(i))
    
    res=max(all_occupied)
    print(f"the maximum occupied seat is number {res}")
    result =find_missing_seat(all_occupied)
    print(f"my seat is number {result}")

test()
main()