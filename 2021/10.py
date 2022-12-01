import common
from collections import Counter
def test():
    inputs="[({(<(())[]>[[{[]{<()<>>\n\
[(()[<>])]({[<{<<[]>>(\n\
{([(<{}[<>[]}>{[]{[(<()>\n\
(((({<>}<{<{<>}{[]{[]{}\n\
[[<[([]))<([[{}[[()]]]\n\
[{[{({}]{}}([{[{{{}}([]\n\
{<[[]]>}<{[{[{[]{()[[[]\n\
[<(<(<(<{}))><([]([]()\n\
<{([([[(<>()){}]>(<<{{\n\
<{([{{}}[<[[[<>{}]]]>[]]".splitlines()
    list_opening=["(","[","{","<"]
    list_ending=[")","]","{","<"]

    rejected_line={}
    valid_line={}
    incomplet_line={}
    for i,input in enumerate(inputs):
        counter=Counter(input)
        # print(counter)
        total=sum(counter.values())
        if total % 2 >0:
            incomplet_line[i]=input
        else:
            if counter["("] == counter[")"] and counter["["] == counter["]"] and counter["{"] == counter["}"] and counter["<"] == counter[">"]:
                valid_line[i]=input
            else:
                print(counter["("] == counter[")"])
                print(counter["["] == counter["]"])
                print(counter["{"] == counter["}"])
                print(counter["<"] == counter[">"])
                print(input)                
                rejected_line[i]=input
    print(rejected_line)
test()
