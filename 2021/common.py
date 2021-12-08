import requests

SESSIONID="53616c7465645f5f88609cee795347a9c3774024e79bbbf2249836f5e4b870c74e94fc46e62f155fc71ca95e7db89efa"

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

def parse_data_by_groups(datas):
    group=list()
    group_lines=datas.split("\n\n")
    for line_group in group_lines:
        group.append([line for line in line_group.split("\n")])           
    return group

def convert_input_to_integer(inputs):
    return [int(item) for item in inputs]

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