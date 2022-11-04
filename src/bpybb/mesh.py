"""
This module contains utilities for working with bmesh objects (Blender's mesh data representation).
"""

import bpy
import bmesh
import mathutils

from bpybb.utils import edit_mode


def get_vert_coordinates_list(obj):
    coordinates_list = []
    with edit_mode():
        bm = bmesh.from_edit_mesh(obj.data)
        for vert in bm.verts:
            vector = mathutils.Vector((vert.co.x, vert.co.y, vert.co.z))
            coordinates_list.append(vector)

    return coordinates_list


def subdivide(number_cuts=1, smoothness=0):
    with edit_mode():
        bpy.ops.mesh.select_all(action="SELECT")
        bpy.ops.mesh.subdivide(number_cuts=number_cuts, smoothness=smoothness)
