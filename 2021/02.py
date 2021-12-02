import common

def part1(inputs,position):
    
    for input in inputs:
        decoded_value=input.decode("utf-8")
        if decoded_value.startswith("f"):
            position[0]+=int(decoded_value.split(" ")[1])            
        elif decoded_value.startswith("u"):
            position[1]+=int(decoded_value.split(" ")[1])            
        elif decoded_value.startswith("d"):
            position[1]-=int(decoded_value.split(" ")[1])
        else:
            raise ValueError(f"Unknown input {decoded_value}")
    return position
   
def part2(inputs,position):
    aim=0
    for input in inputs:
        decoded_value=input.decode("utf-8")
        if decoded_value.startswith("f"):
            position[0]+=int(decoded_value.split(" ")[1])
            position[1]+=int(decoded_value.split(" ")[1])*aim     
        elif decoded_value.startswith("u"):
            aim-=int(decoded_value.split(" ")[1])            
        elif decoded_value.startswith("d"):
            aim+=int(decoded_value.split(" ")[1])
        else:
            raise ValueError(f"Unknown input {decoded_value}")
     
    return position
def calculate_position(position):
    print(abs(position[0]*position[1]))

def test():
    input=b"forward 5\n\
down 5\n\
forward 8\n\
up 3\n\
down 8\n\
forward 2\n"
    inputs=input.splitlines()

    calculate_position(part1(inputs,[0,0]))
    calculate_position(part2(inputs,[0,0]))

def main():
    inputs=common.get_inputs_from_site(2021,2)
    calculate_position(part1(inputs,[0,0]))
    calculate_position(part2(inputs,[0,0]))

test()
main()