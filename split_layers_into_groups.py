#!/usr/bin/env python

from gimpfu import *
import math

image = gimp.image_list()[0]


def create_group_with_layer(layer, groups):
    group = pdb.gimp_layer_group_new(image)
    group.name = layer.name + " group"
    groups[int(layer.name)] = group
    image.add_layer(group, 0)
    copy = pdb.gimp_layer_copy(layer, 1)
    pdb.gimp_image_insert_layer(image, copy, group, 0)
    image.remove_layer(layer)


def add_layer_to_group_of_n(layer, groups, n):
    key = int((int(layer.name) - 1) / n) * n + 1
    group = groups[key]
    copy = pdb.gimp_layer_copy(layer, 1)
    pdb.gimp_image_insert_layer(image, copy, group, 0)
    image.remove_layer(layer)


def create_groups_of_n_layers(n):
    groups = {}
    for l in image.layers:
        if not pdb.gimp_item_is_group(l) and int(l.name) % n == 1:
            create_group_with_layer(l, groups)
        elif not pdb.gimp_item_is_group(l):
            add_layer_to_group_of_n(l, groups, n)


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


def merge_layers_in_groups(image, layers):
    size = len(layers)
    next = layers[0]
    for i in range(1, size):
        next = pdb.gimp_image_merge_down(image, next, 0)
    copy = pdb.gimp_layer_copy(next, 1)
    pdb.gimp_image_insert_layer(image, copy, None, 0)
    image.remove_layer(next)


n = 9
create_groups_of_n_layers(n)
for g in image.layers:
    if pdb.gimp_item_is_group(g):
        position_layers_in_groups_of_n(image, g.layers, n)
        merge_layers_in_groups(image, g.layers)

# layers as pages
