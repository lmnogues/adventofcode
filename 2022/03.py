import common

FULL_LIST="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main_test():
    test_strings="""vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


    lines=test_strings.split("\n")
    first_step(lines)
    second_step(lines)

def main_input():
    lines=common.get_data_from_file("2022/day03.txt")
    lines=lines.split("\n")
    first_step(lines)
    second_step(lines)

def first_step(lines):
    total=0
    for l in lines:
        lenght=int(len(l)/2)
        first=set(l[:lenght])
        second=set(l[lenght:])
        # print(first,second,len(first),len(second))
        intersect=first.intersection(second)
        for i in intersect:        
            total+=(FULL_LIST.index(i)+1)
    print(total)
    return total

def second_step(lines):
    total=0
    groups=[]
    group=list()
    for l in lines:
        group.append(set(l))
        if len(group)==3:
            groups.append(group)
            group=list()
    print(groups)
    for g in groups:
        intersect=g[0].intersection(g[1]).intersection(g[2])        
        print(intersect)
        for i in intersect:        
            total+=(FULL_LIST.index(i)+1)
    print(total)
    return total


main_test()
main_input()