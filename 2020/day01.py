import common
import math


def find_inputs_that_adds_to_total(inputs,total) -> set :
    inputs_result=set()
    for input in inputs:
        if input < total:
            new_total=total-input
            if new_total in inputs:
                inputs_result.add(input)
                inputs_result.add(new_total)
                return inputs_result

def print_result(results):    
    print(f"found values {results} - sum is {sum(results)} multiplication is {math.prod(results)}")



def part1(inputs,total):
    inputs_result=find_inputs_that_adds_to_total(inputs,total)
    print_result(inputs_result)
    return inputs_result

def part2(inputs,total):
    total=2020
    for input in inputs:    
        new_total=total-input
        if new_total > 0 :
            inputs_result=find_inputs_that_adds_to_total(inputs,new_total)
            if inputs_result:
                inputs_result.add(input)
                print_result(inputs_result)
                return inputs_result
    

def main():
    total=2020
    inputs=common.get_input_from_file("day01.txt")
    inputs=common.convert_input_to_integer(inputs)
    results=part1(inputs,total)
    results=part2(inputs,total)

def test():
    total=2020
    inputs=(1721,979,366,299,675,1456)
    results=part1(inputs,total)
    assert results == {1721,299}
    results=part2(inputs,total)
    assert results == {366,979,675}

test()
main()