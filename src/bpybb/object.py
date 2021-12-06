import bpy

from bpybb.utils import active_object, make_active


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
