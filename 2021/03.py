import common

def gamma_epsilon_rate(inputs):
    gamma_rate=""
    epsilon_rate=""
    for i in range(len(inputs[0])):
        count_1=0
        count_0=0
        for input in inputs:
            if int(input[i:i+1])==1:
                count_1+=1
            else:
                count_0+=1
        if count_1 > count_0:
            gamma_rate=gamma_rate+"1"
            epsilon_rate=epsilon_rate+"0"
        else:
            gamma_rate=gamma_rate+"0"
            epsilon_rate=epsilon_rate+"1"
    
    print(gamma_rate)
    print(epsilon_rate)
    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)
    print(gamma_rate * epsilon_rate)

def calculate_oxygen_level(inputs,position=0):
    count_1=0
    count_0=0
    for input in inputs:
        if int(input[position:position+1])==1:
            count_1+=1
        else:
            count_0+=1
    if count_1>=count_0:
        bit_criteria="1"
    else:
        bit_criteria="0"

    filtered_inputs=[x for x in inputs if x[position:position+1]==bit_criteria]
    if len(filtered_inputs)==1:
        return filtered_inputs
    else:
        return calculate_oxygen_level(filtered_inputs,position+1)

def calculate_co2_level(inputs,position=0):
    count_1=0
    count_0=0
    for input in inputs:
        if int(input[position:position+1])==1:
            count_1+=1
        else:
            count_0+=1
    if count_1>= count_0:
        bit_criteria="0"
    else:
        bit_criteria="1"

    filtered_inputs=[x for x in inputs if x[position:position+1]==bit_criteria]
    if len(filtered_inputs)==1:
        return filtered_inputs
    else:
        return calculate_co2_level(filtered_inputs,position+1)

    
def test():
    inputs="00100\n\
11110\n\
10110\n\
10111\n\
10101\n\
01111\n\
00111\n\
11100\n\
10000\n\
11001\n\
00010\n\
01010"
    inputs=inputs.splitlines()
    print(inputs)
    gamma_epsilon_rate(inputs)
    oxygen_level = calculate_oxygen_level(inputs)
    co2_level = calculate_co2_level(inputs)
    oxygen_level = (int(oxygen_level[0],2))
    co2_level = (int(co2_level[0],2))
    print(oxygen_level,co2_level, oxygen_level*co2_level)

def main():
    inputs=common.get_inputs_from_site(2021,3)
    gamma_epsilon_rate(inputs)
    oxygen_level = calculate_oxygen_level(inputs)
    co2_level = calculate_co2_level(inputs)
    oxygen_level = (int(oxygen_level[0],2))
    co2_level = (int(co2_level[0],2))
    print(oxygen_level*co2_level)

test()
main()