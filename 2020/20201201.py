import common
import math

inputs=common.get_input_from_file("20201201.txt")
inputs=common.convert_input_to_integer(inputs)

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


total=2020
inputs_result=find_inputs_that_adds_to_total(inputs,total)
print_result(inputs_result)

for input in inputs:    
    new_total=total-input
    if new_total > 0 :
        inputs_result=find_inputs_that_adds_to_total(inputs,new_total)
        if inputs_result:
            inputs_result.add(input)
            print_result(inputs_result)
            break
        