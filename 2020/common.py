def get_input_from_file(file):
    with open(file, "r") as file_object:
        results = file_object.read().splitlines()
        return results

def convert_input_to_integer(inputs):
    return [int(item) for item in inputs]