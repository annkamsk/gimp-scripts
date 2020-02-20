from gimpfu import *


def merge_layers_in_groups(image, layers):
    size = len(layers)
    next = layers[0]
    for i in range(1, size):
        next = pdb.gimp_image_merge_down(image, next, 0)
    copy = pdb.gimp_layer_copy(next, 1)
    pdb.gimp_image_insert_layer(image, copy, None, 0)
    image.remove_layer(next)
