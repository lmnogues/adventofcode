from os import device_encoding
import common
from collections import Counter


def list_counter(inputs,charging_joltage):
    device_joltage=max(inputs)+3
    inputs.append(charging_joltage)
    inputs.append(device_joltage)
    inputs.sort(reverse=True)
    total=[]
    for x in range(len(inputs)-1):
        total.append(inputs[x]-inputs[x+1])
    
    print(device_joltage)
    counter=Counter(total)
    print(counter)
    return counter


def find_comb(inputs,idx,already_seen_result):   
    if idx==len(inputs) -1:
        return 1
    if idx in already_seen_result:
        return already_seen_result[idx]
    ans=0
    for j in range(idx+1,len(inputs)):
        if inputs[j] - inputs[idx] <=3:
            ans+=find_comb(inputs,j,already_seen_result)
    already_seen_result[idx]=ans
    return ans


def test():
    inputs="""16
10
15
5
1
11
7
19
6
12
4"""
    inputs=inputs.splitlines()
    inputs=common.convert_input_to_integer(inputs)

    device_joltage=max(inputs)+3
    counter=list_counter(inputs,0)
    assert 7 == counter[1]
    assert 5 == counter[3]    
    inputs.sort()
    already_seen_result={}
    print(f"total comb : {find_comb(inputs,0,already_seen_result)}")

def test2():
    inputs="""28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""
    inputs=inputs.splitlines()
    inputs=common.convert_input_to_integer(inputs)

    counter=list_counter(inputs,0)
    assert 22 == counter[1]
    assert 10 == counter[3]
    inputs.sort()
    print(f"total comb : {find_comb(inputs,0,{})}")

def main():
    inputs=common.get_input_from_file("day10.txt") # list
    inputs=common.convert_input_to_integer(inputs)
    counter=list_counter(inputs,0)
    print(counter)
    print(counter[1]*counter[3])
    inputs.sort()
    print(f"total comb : {find_comb(inputs,0,{})}")

test()
test2()
main()