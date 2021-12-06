import bpy

from bpybb.utils import active_object


def apply_material(material):
    obj = active_object()
    obj.data.materials.append(material)


def make_color_ramp_from_color_list(colors, color_ramp_node):
    """
    Creates new sliders on a Color Ramp Node and
    applies the list of colors on each slider
    """
    color_count = len(colors)

    step = 1 / color_count
    cur_pos = step
    # -2 is for the two sliders that are present on the ramp
    for _ in range(color_count - 2):
        color_ramp_node.elements.new(cur_pos)
        cur_pos += step

    for i, color in enumerate(colors):
        color_ramp_node.elements[i].color = color
