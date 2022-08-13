"""
This module contains utilities for working with materials.
"""

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


def apply_emission_material(color, name=None, energy=1):
    material = create_emission_material(color, name=name, energy=energy)

    obj = active_object()
    obj.data.materials.append(material)


def create_emission_material(color, name=None, energy=30, return_nodes=False):
    if name is None:
        name = ""

    material = bpy.data.materials.new(name=f"material.emission.{name}")
    material.use_nodes = True

    out_node = material.node_tree.nodes.get("Material Output")
    bsdf_node = material.node_tree.nodes.get("Principled BSDF")
    material.node_tree.nodes.remove(bsdf_node)

    node_emission = material.node_tree.nodes.new(type="ShaderNodeEmission")
    node_emission.inputs["Color"].default_value = color
    node_emission.inputs["Strength"].default_value = energy

    node_emission.location = 0, 0

    material.node_tree.links.new(node_emission.outputs["Emission"], out_node.inputs["Surface"])

    if return_nodes:
        return material, material.node_tree.nodes
    else:
        return material


def apply_reflective_material(color, name=None, roughness=0.1, specular=0.5):
    material = create_reflective_material(color, name=name, roughness=roughness, specular=specular)

    obj = active_object()
    obj.data.materials.append(material)


def create_reflective_material(color, name=None, roughness=0.1, specular=0.5, return_nodes=False):
    if name is None:
        name = ""

    material = bpy.data.materials.new(name=f"material.reflective.{name}")
    material.use_nodes = True

    material.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = color
    material.node_tree.nodes["Principled BSDF"].inputs["Roughness"].default_value = roughness
    material.node_tree.nodes["Principled BSDF"].inputs["Specular"].default_value = specular

    if return_nodes:
        return material, material.node_tree.nodes
    else:
        return material
