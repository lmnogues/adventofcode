import common
from collections import Counter

def count_rules_part1(list_of_groups):
    list_of_group_ans=list()
    for group in list_of_groups:
        list_ans=set()
        for ppl in group:
            if len(ppl) > 1:
                for ans in ppl:
                    list_ans.add(ans)
            else:
                list_ans.add(ppl)
        list_of_group_ans=list_of_group_ans+list(list_ans)
        # print(f"{group=} {list_ans=}")
    
    return len(list_of_group_ans)

def count_rules_part2(groups):
    global_count=0
    for group in groups:
        ans_count=0
        if len(group)==1:
            ans_count=len(group[0])
        else:
            list_ans=list()
            for ppl in group:
                if len(ppl) > 1:
                    for ans in ppl:
                        list_ans.append(ans)
                else:
                    list_ans.append(ppl)
            counter=Counter(list_ans)
            ans_count=len([x for x,v in counter.items() if v==len(group)])
        global_count+=ans_count
        # print(f"{group=} {ans_count=} {global_count=}")
    return global_count


def test():
    inputs="""abc

a
b
c

ab
ac

a
a
a
a

b"""
    print(inputs)
    groups=common.parse_data_by_groups(inputs)
    assert 11 == count_rules_part1(groups)
    assert 6 == count_rules_part2(groups)

def main():
    inputs=common.get_data_from_file("day06.txt")
    
    groups=common.parse_data_by_groups(inputs)
    print(count_rules_part1(groups))
    print(count_rules_part2(groups))
test()
main()