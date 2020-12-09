from ast import walk
import re
import common

class Luggage:

    def __init__(self,color,) -> None:
        super().__init__()
        self.color=color
        self.child_luggage=dict()
        self.parent_luggage=list()
        self.walked_colors=set()
        self.walked_child=set()
        self.total_child_count=0
    
    def add_child_luggage(self,child_luggage,count):
        lugg=self.child_luggage.get(Luggage,None)
        if lugg is None:
            self.child_luggage[child_luggage]=int(count)
        else:
            self.child_luggage[child_luggage]+=int(count)
        child_luggage.parent_luggage.append(self)

    @property
    def child_count(self):
        return sum([x for x in self.child_luggage.values()])

    def __str__(self) -> str:
        return f"{self.color} : {len(self.child_luggage)}"
    
    def __repr__(self) -> str:
        return self.__str__()

def parse_child_luggage(child,luggage,dict_luggage):
    for c in child.split(","):
        res=re.findall(r"(?P<count>\d+) (?P<color>.*) bags*\.*",c)
        if len(res)>0:
            lugg=dict_luggage.get(res[0][1],None)
            if lugg is None:
                lugg=Luggage(res[0][1])
                dict_luggage[res[0][1]]=lugg
            luggage.add_child_luggage(lugg,res[0][0])            


def walk_parents(lugg):
    if len(lugg.parent_luggage)>0:
        for p in lugg.parent_luggage:
            if p.color not in lugg.walked_colors:
                lugg.walked_colors.add(p.color)
                walk_parents(p)
                lugg.walked_colors.update(p.walked_colors)

def walk_child(lugg):
    if len(lugg.child_luggage)>0:
        for child,count in lugg.child_luggage.items():    
            if child.color not in lugg.walked_child:
                lugg.walked_child.add(child.color)
                lugg.total_child_count+=count
                walk_child(child)
                lugg.total_child_count+=child.total_child_count*count            
                #print(f"{lugg.color} --> {count=} --> {lugg.total_child_count=}--> {child.total_child_count=}")
            


def parse_rules(rules,dict_luggage):
    for rule in rules:
        res=re.findall(r"(?P<bags>.*) bags contain (?P<child_bags>.*)",rule)
        if len(res)>0:
            lugg=dict_luggage.get(res[0][0],None)
            if lugg is None:
                lugg=Luggage(res[0][0])
                dict_luggage[res[0][0]]=lugg
            
            parse_child_luggage(res[0][1],lugg,dict_luggage)
    for k,lugg in dict_luggage.items():
        walk_parents(lugg)
        # print(f"{lugg.color=}  {lugg.walked_colors=} {len(lugg.child_luggage)} , {lugg.child_count=}")
        # print("")
    
    


def test():
    inputs="""light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

    dict_luggage=dict()
    parse_rules(inputs.splitlines(),dict_luggage)
    shiny=dict_luggage.get("shiny gold")
    assert 4 == len(shiny.walked_colors)

    nb_lugg=0
    for child,count in shiny.child_luggage.items():
        nb_lugg+=(child.child_count*count)+count
    assert 32 == nb_lugg

    # walk_child(shiny)
    walk_child(shiny)
    assert 32 == shiny.total_child_count
    

def test2():
    inputs="""shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""

    dict_luggage=dict()
    parse_rules(inputs.splitlines(),dict_luggage)
    shiny=dict_luggage.get("shiny gold")

    walk_child(shiny)
    assert 126 == shiny.total_child_count
    

def main():
    dict_luggage=dict()
    inputs=common.get_input_from_file("day07.txt")
    parse_rules(inputs,dict_luggage)
    shiny=dict_luggage.get("shiny gold")

    walk_child(shiny)
    print(shiny.total_child_count)

test()    
test2()
main()