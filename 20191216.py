
def get_input_from_file(file):
    with open(file, "r") as file_object:
        results = file_object.read().splitlines()
        return results


def complete_missing_pattern(pattern, lenght):
    if len(pattern) >= lenght:
        return pattern
    else:
        final_pattern = list()
        pos = 0
        for i in range(lenght):
            final_pattern.append(pattern[pos])
            pos += 1
            if pos > len(pattern)-1:
                pos = 0
        return final_pattern


def calculate_signal(input_signal, nb_phase):
    signal = []
    for c in input_signal:
        signal.append(c)

    pattern = ['0', '1', '0', '-1']
    for phase in range(nb_phase):
        #print("Input : ", signal)
        result_signal = list()
        for i in range(1, len(signal)+1):
            current_pattern = list()
            for j in range(i):
                current_pattern.append(pattern[0])
            for j in range(i):
                current_pattern.append(pattern[1])
            for j in range(i):
                current_pattern.append(pattern[2])
            for j in range(i):
                current_pattern.append(pattern[3])
            current_pattern = complete_missing_pattern(current_pattern, len(signal)+1)
            current_pattern = current_pattern[1:]
            # print(i, " : ", current_pattern)
            result = 0
            for k in range(len(signal)):
                result += int(signal[k])*int(current_pattern[k])
            result_signal.append(str(result)[-1])
        signal = result_signal
        # print("Output:", signal)
    last_signal = ''.join(signal)
    return last_signal


if __name__ == "__main__":
    inputs = get_input_from_file('20191216.txt')[0]

    input_signal = "12345678"
    last_signal = calculate_signal(input_signal, 4)
    assert last_signal[0:8] == "01029498"

    input_signal = "80871224585914546619083218645595"
    last_signal = calculate_signal(input_signal, 100)
    assert last_signal[0:8] == "24176176"

    input_signal = "19617804207202209144916044189917"
    last_signal = calculate_signal(input_signal, 100)
    assert last_signal[0:8] == "73745418"

    input_signal = "69317163492948606335995924319873"
    last_signal = calculate_signal(input_signal, 100)
    assert last_signal[0:8] == "52432133"

    last_signal = calculate_signal(inputs, 100)
    print(last_signal[0:8])

    # input_signal = "80871224585914546619083218645595" * 10000
    # offset = input_signal[0:7]
    # last_signal = calculate_signal(input_signal, 100)
    # assert last_signal[offset::8] == "84462026"

    # input_signal = "19617804207202209144916044189917" * 10000
    # offset = input_signal[0:7]
    # last_signal = calculate_signal(input_signal, 100)
    # assert last_signal[offset::8] == "78725270"

    # input_signal = "69317163492948606335995924319873" * 10000
    # offset = input_signal[0:7]
    # last_signal = calculate_signal(input_signal, 100)
    # assert last_signal[offset::8] == "53553731"
