import common
import re

class Node:
    def __init__(self,name,parent=None,size=0,children=None,is_dir=True) -> None:
        self.name=name
        self.parent=parent
        self.size=size
        self.children=list()
        self.is_dir=is_dir
        if self.parent:
            self.parent.children.append(self)
    
    def display_tree(self,depth=0,only_dir=False):
        tab=" "*depth
        if only_dir:
            if self.is_dir:
                print(f"{tab}|- {self.name} ({self.size})")        
        else:
            print(f"{tab}|- {self.name} ({self.size})")        

        for c in self.children:            
            c.display_tree(depth+1,only_dir)

    def compile_size(self):
        for c in self.children:
            self.size+=c.compile_size()
        return self.size
    
    def search_dir_by_size(self,size_limit=100000):
        total=list()
        for c in self.children:
            if c.is_dir:
                if c.size < size_limit:
                    total.append(c.size)
            total=total+c.search_dir_by_size(size_limit)
        return total
    
    def find_dir_to_delete(self,required_space,available_space):
        possible_dir=list()
        if self.size +available_space >=required_space:
            possible_dir.append(self)
        for c in self.children:
            if c.is_dir:
                possible_dir=possible_dir+c.find_dir_to_delete(required_space,available_space)
        return possible_dir

    def __str__(self) -> str:
        return f"{self.name} ({self.is_dir} - {self.size})"
    

    def __repr__(self) -> str:
        return f"{self.name} ({self.is_dir} - {self.size})"
    
inputs="""$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

TOTAL_SIZE=70000000
REQUIRED_SIZE=30000000

def viz_dir(input_lines):
    tree_dir=list()
    tree_size=dict()
    first_tree=None
    current_dir=None
    for line in input_lines:
        if line.startswith("$"):
            print("COMMAND : ",line)
            if line=="$ cd /":
                current_dir=Node("/")
                first_tree=current_dir
            elif line=="$ cd ..":
                current_dir=current_dir.parent
            elif line.startswith("$ cd"):
                new_dir=line.replace("$ cd","")
                current_dir=Node(new_dir,current_dir)
        elif line.startswith("dir"):
            print("directory! ",line)
        else:
            print("file !",line)
            infos=re.findall(r"(\d+)\s(.+)",line)
            node=Node(infos[0][1],parent=current_dir,size=int(infos[0][0]),is_dir=False)
    first_tree.compile_size()
    first_tree.display_tree()
    first_tree.display_tree(only_dir=True)
    print(sum(first_tree.search_dir_by_size()))
    available_space=TOTAL_SIZE-first_tree.size
    print(f"/ size : {first_tree.size} - available space={available_space}")
    possible_dir_to_delete = first_tree.find_dir_to_delete(REQUIRED_SIZE,available_space)
    print(min(possible_dir_to_delete,key=lambda x: x.size))

viz_dir(inputs.splitlines())

input_day=common.get_input_from_file("./2022/07.txt")
viz_dir(input_day)