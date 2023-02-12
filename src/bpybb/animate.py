"""
This module contains utilities for speeding up animation creation.
"""

import math
import random

import bpy_types
import mathutils

from bpybb.utils import active_object


def set_fcurve_extrapolation_to_linear(obj: bpy_types.Object = None) -> None:
    """
    Loops over all the fcurves of an action
    and sets the extrapolation to "LINEAR".
    """
    if obj is None:
        obj = active_object()

    for fcurve in obj.animation_data.action.fcurves:
        fcurve.extrapolation = "LINEAR"


def set_fcurve_interpolation_to_linear(obj: bpy_types.Object = None) -> None:
    """
    Loops over all the fcurve key frame points of an action
    and sets the interpolation to "LINEAR".
    """
    if obj is None:
        obj = active_object()

    for fcurve in obj.animation_data.action.fcurves:
        for keyframe_point in fcurve.keyframe_points:
            keyframe_point.interpolation = "LINEAR"


def add_fcruve_cycles_modifier(obj: bpy_types.Object = None) -> None:
    """
    Apply a cycles modifier to all the fcurve animation data of an object.
    """
    if obj is None:
        obj = active_object()

    for fcurve in obj.animation_data.action.fcurves.values():
        modifier = fcurve.modifiers.new(type="CYCLES")
        modifier.mode_before = "REPEAT"
        modifier.mode_after = "REPEAT"


def animate_360_rotation(axis_index, last_frame, obj=None, clockwise=False, linear=True, start_frame=1):
    animate_rotation(360, axis_index, last_frame, obj, clockwise, linear, start_frame)


def animate_rotation(angle, axis_index, last_frame, obj=None, clockwise=False, linear=True, start_frame=1):
    if not obj:
        obj = active_object()
    frame = start_frame
    obj.keyframe_insert("rotation_euler", index=axis_index, frame=frame)

    if clockwise:
        angle_offset = -angle
    else:
        angle_offset = angle
    frame = last_frame
    obj.rotation_euler[axis_index] = math.radians(angle_offset) + obj.rotation_euler[axis_index]
    obj.keyframe_insert("rotation_euler", index=axis_index, frame=frame)

    if linear:
        set_fcurve_extrapolation_to_linear()


def create_data_animation_loop(obj, data_path, start_value, mid_value, start_frame, loop_length, linear_extrapolation=True):
    """
    To make a data property loop we need to:
    1. set the property to an initial value and add a keyframe in the beginning of the loop
    2. set the property to a middle value and add a keyframe in the middle of the loop
    3. set the property the initial value and add a keyframe at the end of the loop
    """

    # set the start value
    setattr(obj, data_path, start_value)
    # add a keyframe at the start
    obj.keyframe_insert(data_path, frame=start_frame)

    # set the middle value
    setattr(obj, data_path, mid_value)
    # add a keyframe in the middle
    mid_frame = start_frame + (loop_length) / 2
    obj.keyframe_insert(data_path, frame=mid_frame)

    # set the end value
    setattr(obj, data_path, start_value)
    # add a keyframe in the end
    end_frame = start_frame + loop_length
    obj.keyframe_insert(data_path, frame=end_frame)

    if linear_extrapolation:
        set_fcurve_extrapolation_to_linear()


def animate_up_n_down_bob(
    start_value: mathutils.Vector, mid_value: mathutils.Vector, obj: bpy_types.Object = None, loop_length: int = 90, start_frame: int = random.randint(0, 60)
) -> None:
    """Animate the up and down bobbing motion of an object. Apply a fcurve cycles modifier to make it seamless."""
    if obj is None:
        obj = active_object()

    create_data_animation_loop(
        obj,
        "location",
        start_value=start_value,
        mid_value=mid_value,
        start_frame=start_frame,
        loop_length=loop_length,
        linear_extrapolation=False,
    )

    add_fcruve_cycles_modifier(obj)
