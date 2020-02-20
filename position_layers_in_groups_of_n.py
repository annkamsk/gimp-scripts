from gimpfu import *
import math


def scale_layer(layer, r):
    new_width = layer.width / r
    new_height = layer.height / r
    pdb.gimp_layer_scale(layer, new_width, new_height, True)


def position_layers_in_groups_of_n(image, layers, n):
    k = int(math.sqrt(n))
    dx = image.width / k
    dy = image.height / k
    i = 0
    for l in layers:
        scale_layer(l, k)
        x = (i % k) * dx
        y = (i / k) * dy
        l.set_offsets(x, y)
        i = i + 1
