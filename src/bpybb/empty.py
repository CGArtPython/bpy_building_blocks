"""
This module contains utilities working with Blender collections.
"""

import bpy

from bpybb.utils import active_object


def add_ctrl_empty(name=None):

    bpy.ops.object.empty_add(type="PLAIN_AXES")
    empty_ctrl = active_object()

    if name:
        empty_ctrl.name = f"empty.{name}"
    else:
        empty_ctrl.name = "empty.cntrl"

    return empty_ctrl
