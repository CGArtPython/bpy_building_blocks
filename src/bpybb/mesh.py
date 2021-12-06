import bmesh
import mathutils

from bpybb.utils import editmode


def get_vert_coordinates_list(obj):
    coordinates_list = []
    with editmode():
        bm = bmesh.from_edit_mesh(obj.data)
        for vert in bm.verts:
            vector = mathutils.Vector((vert.co.x, vert.co.y, vert.co.z))
            coordinates_list.append(vector)

    return coordinates_list
