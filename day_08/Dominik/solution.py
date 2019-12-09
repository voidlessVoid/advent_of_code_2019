def read_input_to_list(path):
    with open(path, "r") as f:
        content = f.readline()
    return content


content = read_input_to_list("input.txt")

image_size = (25, 6)


def layer_splitting(image_data, size: int):
    start = 0
    for i in range(0, len(image_data), size):
        yield image_data[start:start + size]
        start += size


splitted_image = list(layer_splitting(image_data=content, size=image_size[0]))
layered_image = list(layer_splitting(image_data=splitted_image, size=image_size[1]))


def checksum(image_data):
    def counter(layer, pattern: str):
        count = 0
        for row in layer:
            count += row.count(pattern)
        return count

    dic = {}
    for layer in image_data:
        zero = counter(layer=layer, pattern="0")
        dic[zero] = layer

    check = counter(layer=dic[min(dic.keys())], pattern="1") * counter(layer=dic[min(dic.keys())], pattern="2")
    print(f"The checksum for the image is: {check}")


# checksum(image_data=layered_image)
import copy
def decode_image(image_data):
    image_data_reversed = image_data[::-1]
    for i, layer in enumerate(image_data_reversed.copy()):
       for m, row in enumerate(layer):
           image_data_reversed[i][m]= list(row)

    for i, layer in enumerate(image_data_reversed.copy()):
        if i > 0:
            print(f"Layer {i}")
            for nrow in range(len(layer)):
                top_layer = image_data_reversed[i][nrow]
                lower_layer = image_data_reversed[i - 1][nrow]
                for n,char in enumerate(top_layer.copy()):
                    if char == "2":
                        top_layer[n] = lower_layer[n]

    return image_data_reversed[-1]

image= decode_image(image_data=layered_image)
# correct answer CFLUL
# conditional formatting in Excel for visualisation