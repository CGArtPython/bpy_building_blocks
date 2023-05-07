"""
This module contains utilities for working with Blender objects.
"""

import math

import bpy

import bpy_types

from bpybb.utils import active_object, make_active, deselect_all_objects
from bpybb.addon import enable_extra_meshes


def join_objects(objects: list[bpy_types.Object]) -> bpy_types.Object:
    deselect_all_objects()

    for obj in objects:
        obj.select_set(True)

    bpy.ops.object.join()

    new_obj = active_object()

    return new_obj


def rotate_object(axis: int, degrees: float) -> None:
    bpy.context.active_object.rotation_euler[axis] = math.radians(degrees)


def apply_location():
    bpy.ops.object.transform_apply(location=True)


def add_empty(name=None):
    bpy.ops.object.empty_add(type="PLAIN_AXES")
    empty_obj = active_object()
    if name:
        empty_obj.name = name
    else:
        empty_obj.name = "empty.cntrl"
    return empty_obj


def track_empty(obj):
    empty_target = add_empty(name="empty.tracker-target")

    make_active(obj)
    bpy.ops.object.constraint_add(type="TRACK_TO")
    bpy.context.object.constraints["Track To"].target = empty_target

    return empty_target


def add_bezier_circle(radius: float = 1.0, bevel_depth: float = 0.0, resolution_u: int = 12, extrude: float = 0.0) -> bpy_types.Object:
    """Adds a Bezier circle curve into the scene.

    Args:
        radius (float, optional): the radius of the circle. Defaults to 1.
        bevel_depth (float, optional): the size of the bevel (the bevel is off if this is 0). Defaults to 0.
        resolution_u (int, optional): the number of computed points between two control points. Defaults to 12.

    Returns:
        bpy_types.Object: a reference to the created Bezier circle curve object
    """
    bpy.ops.curve.primitive_bezier_circle_add(radius=radius)

    bezier_circle_obj = active_object()

    bezier_circle_obj.data.bevel_depth = bevel_depth
    bezier_circle_obj.data.resolution_u = resolution_u
    bezier_circle_obj.data.extrude = extrude

    return bezier_circle_obj


def add_round_cube(radius: float = 1.0) -> bpy_types.Object:
    """Adds a Round Cube into the scene.

    Args:
        radius (float, optional): the radios of the Round Cube. Defaults to 1.0.

    Returns:
        bpy_types.Object: a reference to the created Round Cube curve object
    """
    enable_extra_meshes()
    bpy.ops.mesh.primitive_round_cube_add(radius=radius)
    return active_object()


def add_subdivided_round_cube(radius: float = 1.0) -> tuple[bpy_types.Object, bpy.types.SubsurfModifier]:
    """Adds a Round Cube into the scene and applies a Subdivision modifier.

    Args:
        radius (float, optional): the radios of the Round Cube. Defaults to 1.0.

    Returns:
        bpy_types.Object: a reference to the created Round Cube curve object
    """
    round_cube_obj = add_round_cube(radius)

    bpy.ops.object.modifier_add(type="SUBSURF")

    return round_cube_obj, round_cube_obj.modifiers["Subdivision"]
