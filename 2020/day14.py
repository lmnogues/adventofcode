import common

def apply_mask(mask,val):
    for i,m in enumerate(mask):
        if m!="X":
            val[i]=m
    return val
def apply_all_masks(mem_mask):
    memory_transformed={}
    for k,v in mem_mask.items():
        # memory_transformed[k]={}
        mask=v[0].split("=")[1].strip()
        test_mem=v[1:]
        memory={}
        for m in test_mem:
            pos= int(m.split("[")[1].split("]")[0])
            val=list("{0:036b}".format(int(m.split("=")[1])))
            memory[pos]=val
        for pos,val in memory.items():
            val = apply_mask(mask,val)
            memory[pos]=val
            memory_transformed[pos]=int("".join(val),2)
           
    return memory_transformed

def parse_inputs(inputs):
    inputs=inputs.splitlines()
    mem_mask={}
    idx=0
    for i in inputs:
        if i.startswith("mask"):
            array=[]
            idx+=1
        else:
            array=mem_mask[idx]
        array.append(i)
        mem_mask[idx]=array
    return mem_mask

def test():
    inputs="""mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""
    mem_mask=parse_inputs(inputs)
    memory_transformed=apply_all_masks(mem_mask)
    assert 165 == sum([x for x in memory_transformed.values()])

def main():
    inputs=common.get_data_from_file("day14.txt")    
    mem_mask=parse_inputs(inputs)
    memory_transformed=apply_all_masks(mem_mask)
    print(sum([x for x in memory_transformed.values()]))
    
test()
main()