import requests

SESSIONID="53616c7465645f5f3efd54d35ffc19e2d6212e4bfcb2862f059f6f2781e46860cd0c9da0ce8974eab8f40a598d2d0f6c76669dff73fe39eae8ee58b18f7caf5c"

def get_data_from_site(year,day):
    response = requests.get(f"https://adventofcode.com/{year}/day/{day}/input",cookies={'session': SESSIONID})   
    return response.content.decode('UTF-8')

def get_inputs_from_site(year,day,split="newline"):
    if split=="newline":
        return get_data_from_site(year,day).splitlines()
    else:
        return get_data_from_site(year,day).split(split)

def get_data_from_file(file):
    with open(file, "r") as file_object:
        return file_object.read()

def get_input_from_file(file):   
    return get_data_from_file(file).splitlines()

def parse_data_by_groups(datas,as_int=False):
    group=list()
    group_lines=datas.split("\n\n")
    for line_group in group_lines:
        values=[line for line in line_group.split("\n")]
        if as_int:
            group.append(convert_input_to_integer(values))
        else:    
            group.append(values)           
    return group

def convert_input_to_integer(inputs):
    try:
        converted_input=[int(item) for item in inputs if item!=""]
        return converted_input
    except Exception as e:
        print(e)
        print(inputs)
    

def get_integer_inputs(file=None,year=None,day=None,split="newline"):
    if year is not None:
        if day is not None:
            return convert_input_to_integer(get_inputs_from_site(year,day,split))
        else:
            raise ValueError("Year & Date should be set")
    if file is not None:
        return convert_input_to_integer(get_input_from_file(file))
    else:
        raise ValueError("at least file or year/date should be set")