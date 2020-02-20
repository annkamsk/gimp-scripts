from gimpfu import *


def create_group_with_layer(image, layer, groups):
    group = pdb.gimp_layer_group_new(image)
    group.name = layer.name + " group"
    groups[int(layer.name)] = group
    image.add_layer(group, 0)
    copy = pdb.gimp_layer_copy(layer, 1)
    pdb.gimp_image_insert_layer(image, copy, group, 0)
    image.remove_layer(layer)


def add_layer_to_group_of_n(image, layer, groups, n):
    key = int((int(layer.name) - 1) / n) * n + 1
    group = groups[key]
    copy = pdb.gimp_layer_copy(layer, 1)
    pdb.gimp_image_insert_layer(image, copy, group, 0)
    image.remove_layer(layer)


def create_groups_of_n_layers(image, n):
    groups = {}
    for l in image.layers:
        if not pdb.gimp_item_is_group(l) and int(l.name) % n == 1:
            create_group_with_layer(image, l, groups)
        elif not pdb.gimp_item_is_group(l):
            add_layer_to_group_of_n(image, l, groups, n)
