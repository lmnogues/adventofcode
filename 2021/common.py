import requests

SESSIONID="53616c7465645f5f3a9ac51f0539a42b5606c2fe0380a915d99b07a6704216895a05829f0b0e094eb6867375e5623c67"

def get_data_from_site(year,day):
    response = requests.get(f"https://adventofcode.com/{year}/day/{day}/input",cookies={'session': SESSIONID})   
    return response.content.decode('UTF-8')

def get_inputs_from_site(year,day):
    return get_data_from_site(year,day).splitlines()

def get_data_from_file(file):
    with open(file, "r") as file_object:
        return file_object.read()

def get_input_from_file(file):   
    return get_data_from_file(file).splitlines()

def parse_data_by_groups(datas):
    group=list()
    group_lines=datas.split("\n\n")
    for line_group in group_lines:
        group.append([line for line in line_group.split("\n")])           
    return group

def convert_input_to_integer(inputs):
    return [int(item) for item in inputs]

def get_integer_inputs(file=None,year=None,day=None):
    if year is not None:
        if day is not None:
            return convert_input_to_integer(get_inputs_from_site(year,day))
        else:
            raise ValueError("Year & Date should be set")
    if file is not None:
        return convert_input_to_integer(get_input_from_file(file))
    else:
        raise ValueError("at least file or year/date should be set")