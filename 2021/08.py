import common

#  0:      1:      2:      3:      4:
# aaaa    ....    aaaa    aaaa    ....
#b    c  .    c  .    c  .    c  b    c
#b    c  .    c  .    c  .    c  b    c
# ....    ....    dddd    dddd    dddd
#e    f  .    f  e    .  .    f  .    f
#e    f  .    f  e    .  .    f  .    f
# gggg    ....    gggg    gggg    ....

#  5:      6:      7:      8:      9:
# aaaa    aaaa    aaaa    aaaa    aaaa
#b    .  b    .  .    c  b    c  b    c
#b    .  b    .  .    c  b    c  b    c
# dddd    dddd    ....    dddd    dddd
#.    f  e    f  .    f  e    f  .    f
#.    f  e    f  .    f  e    f  .    f
# gggg    gggg    ....    gggg    gggg

def analyse_number(inputs):
    all_num=[]
    for i in inputs:
        segments,number=i.split("|")
        segments=[s.strip() for s in segments.split(" ")if s !=""]
        number=[n.strip() for n in number.split(" ") if n !=""]
        print(segments)
        print(number)
        all_num.append(number)
    easy_num=[]
    for x in all_num:
        for n in x:
            if len(n)==2 or len(n)==7 or len(n)==3 or len(n)==4:
                easy_num.append(n)
    print(len(easy_num))

def analyse_segments(inputs):
    total=0
    for i in inputs:
        set_num=dict()
        segments,number=i.split("|")
        segments=sorted([s.strip() for s in segments.split(" ")if s !=""],key=len)
        number=[n.strip() for n in number.split(" ") if n !=""]

        while len(set_num)<10:
            for n in segments:
                temp_set=set()
                temp_set.update(n)
                if len(n)==2 :
                    set_num[1]=temp_set
                if len(n)==3: 
                    set_num[7]=temp_set
                if len(n)==4:
                    set_num[4]=temp_set
                if len(n)==5:
                    if temp_set.issuperset(set_num[7]):
                        set_num[3]=temp_set
                    elif set_num.get(6) and len(set_num[6].difference(temp_set))==1:
                        set_num[5] = temp_set
                    else:
                        set_num[2] = temp_set
                if len(n)==6:
                    if temp_set.issuperset(set_num[4]): # 0 or 9                        
                        set_num[9]=temp_set
                    elif temp_set.intersection(set_num[7]) == set_num[7]:                            
                        set_num[0]=temp_set
                    else:
                        set_num[6]=temp_set
                if len(n)==7 :
                    set_num[8]=temp_set
        print(sorted(set_num.items()))
        result=""
        for num in number:
            num_set=set()
            num_set.update(num)
            for key,val in set_num.items():
                if num_set == val:
                    result+=str(key)
        print(result)
        total+=int(result)
    print(total)
                    
        
def test():
    inputs="be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe\n\
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc\n\
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg\n\
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb\n\
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea\n\
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb\n\
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe\n\
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef\n\
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb\n\
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce".splitlines()
    analyse_number(inputs)
    analyse_segments(inputs)

def test2():
    inputs=["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]
    analyse_number(inputs)
    analyse_segments(inputs)


def main():
    inputs=common.get_inputs_from_site(2021,8)
    analyse_number(inputs)

    analyse_segments(inputs)
test()
test2()
main()