"""
This module contains utilities for working with Blender modifiers.
"""

import bpy
import bpy_types

from bpybb.utils import active_object
from bpybb.empty import add_ctrl_empty


def add_displace_modifier(
    name: str, texture_type: str, empty_obj: bpy_types.Object = None
) -> tuple[bpy.types.DisplaceModifier, bpy.types.Texture, bpy_types.Object]:
    """
    Add a displace modifier and a texture to the currently active object.
    Return the modifier, texture, and empty object to
    control the modifier.
    """
    obj = active_object()

    texture = bpy.data.textures.new(f"texture.{name}", texture_type)

    bpy.ops.object.modifier_add(type="DISPLACE")
    displace_modifier = obj.modifiers["Displace"]
    displace_modifier.texture = texture
    displace_modifier.name = f"displace.{name}"
    displace_modifier.texture_coords = "OBJECT"

    if empty_obj == None:
        empty_obj = add_ctrl_empty()

    empty_obj.name = f"empty.{name}"

    displace_modifier.texture_coords_object = empty_obj

    return displace_modifier, texture, empty_obj
