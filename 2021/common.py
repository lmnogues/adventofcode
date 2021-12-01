def get_data_from_file(file):
    with open(file, "r") as file_object:
        return file_object.read()

def get_input_from_file(file):   
    with open(file, "r") as file_object: 
        return file_object.read().splitlines()         

def parse_data_by_groups(datas):
    group=list()
    group_lines=datas.split("\n\n")
    for line_group in group_lines:
        group.append([line for line in line_group.split("\n")])           
    return group

def convert_input_to_integer(inputs):
    return [int(item) for item in inputs]


def get_integer_inputs(file):
    return convert_input_to_integer(get_input_from_file(file))