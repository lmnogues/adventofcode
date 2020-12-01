input_range_min = 372304
input_range_max = 847060


def rule_1_number_increasing(input_number):
    current_max = 0
    for number in str(input_number):
        if int(number) < current_max:
            return False
        current_max = int(number)
    return True


def rule_2_two_occurence(input_number):
    input_nb = str(input_number)
    for i in range(0, 5):
        if input_nb[i] == input_nb[i+1] \
                and (i == 0 or input_nb[i] != input_nb[i-1]) \
                and (i == 4 or input_nb[i] != input_nb[i+2]):
            return True
    return False


def is_valid_input(input_number):
    if rule_2_two_occurence(input_number):
        return rule_1_number_increasing(input_number)
    else:
        return False


def loop_through_inputs(min, max):
    valid_input = list()
    for input_number in range(min, max):
        if is_valid_input(input_number):
            valid_input.append(input_number)
    return valid_input


def test_is_valid_input():
    val = is_valid_input(111111)
    assert val == False

    val = is_valid_input(223450)
    assert val == False

    val = is_valid_input(123789)
    assert val == False

    val = is_valid_input(112233)
    assert val == True

    val = is_valid_input(123444)
    assert val == False

    val = is_valid_input(111122)
    assert val == True


if __name__ == "__main__":
    test_is_valid_input()
    total = loop_through_inputs(input_range_min, input_range_max)
    print("TOTAL : {0}".format(len(total)))
    print(total)
