from gimpfu import *


def add_layer_to_group_of_n(image, layer, groups, n):
    key = int((int(layer.name) - 1) / n) * n + 1
    group = groups[key]
    copy = pdb.gimp_layer_copy(layer, 1)
    pdb.gimp_image_insert_layer(image, copy, group, 0)
    image.remove_layer(layer)
