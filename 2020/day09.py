import common

def sum_of_two(values_to_check):
    all_sums=set()
    for i in range(len(values_to_check)-1):
        for j in range(i,len(values_to_check)):
            all_sums.add(values_to_check[i]+values_to_check[j])
    return all_sums

def find_first_issue(preamble,inputs):
    
    for i in range(preamble,len(inputs)):
        values_to_check=inputs[i-preamble:i]
        all_sums=sum_of_two(values_to_check)
        if not int(inputs[i]) in all_sums:
            return inputs[i]

def find_consecutive_sum(cleaned_inputs,broken_input):
    
    for value in cleaned_inputs:
        result=value
        idx=cleaned_inputs.index(value)
        for sub_val in cleaned_inputs[idx+1:]:
            result+=sub_val
            if result==broken_input:
                idx2=cleaned_inputs.index(sub_val)
                results=cleaned_inputs[idx:idx2+1]
                total=min(results)+max(results)
                print(f"{total} calcualted from {results}")
                return total
            if result > broken_input:
                break


def test():
    inputs="""35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""
    preamble=5
    inputs=common.convert_input_to_integer(inputs.splitlines())
    broken_input=find_first_issue(preamble,inputs)
    assert 127 == broken_input
    cleaned_inputs=[x for x in inputs if x < broken_input]
    assert 62 == find_consecutive_sum(cleaned_inputs,broken_input)

def main():
    inputs=common.get_input_from_file("day09.txt")
    inputs=common.convert_input_to_integer(inputs)
    preamble=25
    broken_input=find_first_issue(preamble,inputs)
    assert 23278925 == broken_input
    cleaned_inputs=[x for x in inputs if x < broken_input]
    assert 4011064 == find_consecutive_sum(cleaned_inputs,broken_input)
test()
main()