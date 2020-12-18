import operator
import common

ops = {
    '+' : operator.add,
    '*' : operator.mul,
}

def evaluate(eq,part1):
    if len(eq)==1:
        return int(eq[0])

    if type(eq[0]) is list:
        left=evaluate(eq[0],part1)
    else:
        left=int(eq[0])
    
    if type(eq[2]) is list:
        right=evaluate(eq[2],part1)
    else:
        right=int(eq[2])

    if part1:        
        op=(eq[1])
        res=(ops.get(op)(left,right))
        if len(eq)>3:
            new_eq=eq[3:]
            new_eq.insert(0,res)
            # print(new_eq)
            res = evaluate(new_eq,part1)
        return res
    else:
        if len(eq)>3:
            eq=handle_prioriti(eq,"+")
            eq=handle_prioriti(eq,"*")
            if len(eq)==1:            
                res=eq[0]
            else :
                res = evaluate(eq,part1)            
            return res
        elif len(eq)==3:            
            op=(eq[1])
            res=(ops.get(op)(left,right))
            return res
        else:
            print("ERROR")

def handle_prioriti(eq,op):
    dict_eq=dict(enumerate(eq))
    
    list_op=[]
    for i,v in dict_eq.items():
        if v in [op] :
            list_op.append(i)
    #all add
    if len(list_op) >0:
        i=list_op[0]
        if type(dict_eq[i-1]) is list:
            left=evaluate(dict_eq[i-1],False)
        else:
            left=int(dict_eq[i-1])
        
        if type(dict_eq[i+1]) is list:
            right=evaluate(dict_eq[i+1],False)
        else:
            right=int(dict_eq[i+1])

        res = (ops.get(op)(left,right))
        dict_eq[i-1]=res
        dict_eq.pop(i)
        dict_eq.pop(i+1)
        if len(eq)>3:
            eq=list(dict_eq.values())
            return handle_prioriti(eq,op)
    
    eq=list(dict_eq.values())
    return eq

def parse_equation(input,start_pos=0,opened_par=False,part1=True):
    eq=[]
    i=start_pos
    while i < len(input):
        v=input[i]
        i+=1        
        if v=="(":
            opened_par=True
            sub_q,next_i=parse_equation(input,i,True,part1)
            eq.append(sub_q)
            i=next_i
        elif v==")":
            if opened_par:
                # print(eq)
                if len(eq)==3:
                    eq=evaluate(eq,part1)
                return eq,i
        elif v==" ":
            continue
        else:
            eq.append(v)
        
    eq=evaluate(eq,part1)
    return eq,i


def test():
    test_inputs=[
    (51,"1 + (2 * 3) + (4 * (5 + 6))"),
    (71,"1 + 2 * 3 + 4 * 5 + 6"),
    (26,"2 * 3 + (4 * 5)"),
    (437,"5 + (8 * 3 + 9 + 3 * 4 * 3)"),
    (12240,"5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"),
    (13632,"((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2")
    ]
    for res,eq in test_inputs:
        rr,_i = parse_equation(eq)
        assert res == rr
    
    test_inputs=[
    (51,"1 + (2 * 3) + (4 * (5 + 6))"),
    (231,"1 + 2 * 3 + 4 * 5 + 6"),
    (46,"2 * 3 + (4 * 5)"),
    (1445,"5 + (8 * 3 + 9 + 3 * 4 * 3)"),
    (669060,"5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"),
    (23340,"((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2")
    ]

    for res,eq in test_inputs:
        print(eq)
        rr,_i = parse_equation(eq,part1=False)
        assert res == rr

    debug=[(2744,"8 * 7 * (3 + (2 * 5 + 8)) + 6 + 8 + 6")]
    
    for res,eq in debug:
        print(eq)
        rr,_i = parse_equation(eq,part1=False)
        assert res == rr

def main():
    inputs=common.get_input_from_file("day18.txt")

    total=0
    for e in inputs:
        res,_ = parse_equation(e)
        total+=res
    assert 75592527415659 == total
    
    total=0
    for e in inputs:
        res,_ = parse_equation(e,part1=False)
        # print(res)
        total+=res
    print(total)

test()
main()