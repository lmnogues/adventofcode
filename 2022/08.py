import common
import math
import copy
test_inputs="""30373
25512
65332
33549
35390"""


def parse_map(inputs):
    map=[]
    for line in inputs.splitlines():
        map.append([int(c) for c in line])

    # print(map)
    return map
def is_visible(x,y,map):    
    if x==0 or x==len(map)-1:
        return True
    if y==0 or y==len(map[x])-1:
        return True

    # left
    tree=map[x][y]
    # print(tree)
    left=max(map[x][0:y])
    right=max(map[x][y+1:])
    top=max([x[y] for x in map[0:x]])
    bottom=max([x[y] for x in map[x+1:]])
    if tree > left:
        return True
    elif tree > right:
        return True
    elif tree > top:
        return True
    elif tree > bottom:
        return True
    return False
def check_line_of_view(tree_view,tree):
    score=list()
    if tree_view and len(tree_view)>0 :
        if max(tree_view) < tree:
            # all left are visible
            score.append(len(tree_view))
        else:
            # at least a tree is blocking
            left_score=0
            for t in tree_view:
                left_score+=1
                if t>=tree:
                    break;        
            score.append(left_score)
    else:
        score.append(0)
    return score

def find_best_tree(map):     
    # print(map)
    result=copy.deepcopy(map)
    for x in range(len(map)):
        for y in range(len(map[x])):
            score=list() 
            tree=map[x][y]
            # print(tree)
            left=map[x][0:y]
            right=map[x][y+1:]
            top=[x[y] for x in map[0:x]]
            bottom=[x[y] for x in map[x+1:]]
            left.reverse()
            top.reverse()
            score=score+(check_line_of_view(left,tree))
            score=score+(check_line_of_view(right,tree))
            score=score+(check_line_of_view(top,tree))
            score=score+(check_line_of_view(bottom,tree))
            # print(f"({x},{y}):{tree} = {score} => {math.prod(score)}")
            result[x][y]=math.prod(score)
    # print(result)
    return result
        
    


def detect_visible_tree(map):
    count_visible=0
    for x in range(len(map)):
        for y in range(len(map[x])):
            if is_visible(x,y,map):
                count_visible+=1
    print(count_visible)

test_map = parse_map(test_inputs)
detect_visible_tree(test_map)
result =find_best_tree(test_map)
print(max([max(x) for x in result]))

inputs=common.get_data_from_file("2022/08.txt")
map=parse_map(inputs)
detect_visible_tree(map)
result =find_best_tree(map)
print(max([max(x) for x in result]))


