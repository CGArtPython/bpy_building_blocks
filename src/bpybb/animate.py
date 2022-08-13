"""
This module contains utilities for speeding up animation creation.
"""

import math

from bpybb.utils import active_object


def set_fcurve_extrapolation_to_linear(obj=None):
    """loops over all the fcurves of an action
    and sets the extrapolation to "LINEAR"
    """
    if obj is None:
        obj = active_object()

    for fc in obj.animation_data.action.fcurves:
        fc.extrapolation = "LINEAR"


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
