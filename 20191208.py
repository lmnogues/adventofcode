def calculate_layers(imageData, width, height):
    input_length = len(imageData)
    image_size = (width * height)
    nb_layer = int(input_length / image_size)
    print(nb_layer)
    pos = 0
    layers = list()
    for _ in range(nb_layer):
        layer = imageData[pos:pos+image_size]
        pos = pos + image_size
        # print(layer)
        layers.append(layer)
    return layers


def validate_image(layers):
    nb_zero = 26
    min_layer = None
    for l in layers:
        count_zero = l.count('0')
        if nb_zero > count_zero:
            nb_zero = count_zero
            min_layer = l

    return min_layer.count('1') * min_layer.count('2')


def process_layers(layers):
    layers.reverse()
    final_layer = [c for c in layers[0]]

    for layer in layers:
        for i in range(len(layer)):
            if layer[i] != '2':
                final_layer[i] = layer[i]
    return ''.join(final_layer)


def get_input_from_file(file):
    with open(file, "r") as file_object:
        results = file_object.read().splitlines()
        return results


layers = calculate_layers('0222112222120000', 2, 2)
finalImage = process_layers(layers)
assert finalImage == '0110'

inputs = get_input_from_file('20191208.txt')
imageData = inputs[0]
layers = calculate_layers(imageData, 25, 6)
assert validate_image(layers) == 2562
finalImg = process_layers(layers)
print(finalImg)
pos = 0
for _ in range(6):
    layer = finalImg[pos:pos+25]
    pos = pos + 25
    layer = layer.replace('0', ' ')
    layer = layer.replace('1', '#')
    print(layer)
