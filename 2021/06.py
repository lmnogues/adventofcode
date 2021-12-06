import common
from collections import defaultdict, Counter

def process(inputs,duration=80):    
    total_count=inputs
    for day in range(duration):
        count_of_day=defaultdict(int)
        for val,count in total_count.items():
            if val == 0:
                count_of_day[6]+=count
                count_of_day[8]+=count
            else:
                count_of_day[val-1]+=count
        total_count=count_of_day
    return total_count
    

def test():
    inputs=Counter([int(x) for x in "3,4,3,1,2".split(",")])
    print(inputs)
    print(sum(process(inputs).values()))
    print(sum(process(inputs,256).values()))
    # res = None
    # for i in range(80):
    #     res = process(inputs)
    # print(len(res))

def main():
    inputs=Counter(common.get_integer_inputs(year=2021,day=6,split=","))
    print(sum(process(inputs).values()))
    print(sum(process(inputs,256).values()))
    # res = None
    #     res = process(inputs)
    # print(len(res))

test()
main()