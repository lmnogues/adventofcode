import common


def count_increase(inputs)->int:
    result=0
    prev=None
    for i in inputs:
        if prev is None:
            prev = i
            pass
        else:
            if i > prev:
                result+=1
            prev=i
    print(result)
    return result
        
def count_increase_per_group(inputs,step=3):
    result=0
    prev=None
    for i in range(len(inputs)):
        sum_next_step=sum(inputs[i:i+3])
        if prev is None:
            prev = sum_next_step
            pass
        else:
            if sum_next_step > prev:
                result+=1
            prev=sum_next_step
    print(result)
    return result

def main():
    inputs=common.get_integer_inputs("./2021/01.txt")
    count_increase(inputs)
    count_increase_per_group(inputs)
    

def test():
    inputs=(199,200,208,210,200,207,240,269,260,263)
    assert count_increase(inputs) == 7 
    assert count_increase_per_group(inputs) == 5 

    


test()
main()