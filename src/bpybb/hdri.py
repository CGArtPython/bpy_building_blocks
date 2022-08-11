"""
This module contains utilities for working with HDRIs.
"""

import bpy


def apply_hdri(path_to_image, bg_color, hdri_light_strength, bg_strength):
    """
    Based on a technique from a FlippedNormals tutorial
    https://www.youtube.com/watch?v=dbAWTNCJVEs
    """
    world_node_tree = bpy.context.scene.world.node_tree

    nodes_to_remove = []
    for node in world_node_tree.nodes:
        nodes_to_remove.append(node)

    for node in nodes_to_remove:
        world_node_tree.nodes.remove(node)

    location_x = 0
    texture_coordinate_node = world_node_tree.nodes.new(type="ShaderNodeTexCoord")
    texture_coordinate_node.name = "Texture Coordinate"
    texture_coordinate_node.location.x = location_x
    location_x += 200

    mapping_node = world_node_tree.nodes.new(type="ShaderNodeMapping")
    mapping_node.location.x = location_x
    location_x += 200
    mapping_node.name = "Mapping"

    environment_texture_node = world_node_tree.nodes.new(type="ShaderNodeTexEnvironment")
    environment_texture_node.location.x = location_x
    location_x += 300
    environment_texture_node.name = "Environment Texture"
    environment_texture_node.image = bpy.data.images.load(path_to_image)

    background_node = world_node_tree.nodes.new(type="ShaderNodeBackground")
    background_node.location.x = location_x
    background_node.name = "Background"
    background_node.inputs["Strength"].default_value = hdri_light_strength

    background_node_2 = world_node_tree.nodes.new(type="ShaderNodeBackground")
    background_node_2.location.x = location_x
    background_node_2.location.y = -100
    background_node_2.name = "Background.001"
    background_node_2.inputs["Color"].default_value = bg_color
    background_node_2.inputs["Strength"].default_value = bg_strength

    light_path_node = world_node_tree.nodes.new(type="ShaderNodeLightPath")
    light_path_node.location.x = location_x
    light_path_node.location.y = 400
    location_x += 200
    light_path_node.name = "Light Path"

    mix_shader_node = world_node_tree.nodes.new(type="ShaderNodeMixShader")
    mix_shader_node.location.x = location_x
    location_x += 200
    mix_shader_node.name = "Mix Shader"

    world_output_node = world_node_tree.nodes.new(type="ShaderNodeOutputWorld")
    world_output_node.location.x = location_x
    location_x += 200

    # links begin
    from_node = background_node
    to_node = mix_shader_node
    world_node_tree.links.new(from_node.outputs["Background"], to_node.inputs["Shader"])

    from_node = mapping_node
    to_node = environment_texture_node
    world_node_tree.links.new(from_node.outputs["Vector"], to_node.inputs["Vector"])

    from_node = texture_coordinate_node
    to_node = mapping_node
    world_node_tree.links.new(from_node.outputs["Generated"], to_node.inputs["Vector"])

    from_node = environment_texture_node
    to_node = background_node
    world_node_tree.links.new(from_node.outputs["Color"], to_node.inputs["Color"])

    from_node = background_node_2
    to_node = mix_shader_node
    world_node_tree.links.new(from_node.outputs["Background"], to_node.inputs[2])

    from_node = light_path_node
    to_node = mix_shader_node
    world_node_tree.links.new(from_node.outputs["Is Camera Ray"], to_node.inputs["Fac"])

    from_node = mix_shader_node
    to_node = world_output_node
    world_node_tree.links.new(from_node.outputs["Shader"], to_node.inputs["Surface"])
    # links end

    return world_node_tree
