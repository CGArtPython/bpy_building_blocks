"""
This module contains common helper utilities.
"""

import contextlib

import bpy


class Axis:
    """Helper class to make code working with axis more readable."""

    X = 0
    Y = 1
    Z = 2


def active_object():
    """
    returns the currently active object
    """
    return bpy.context.active_object


def make_active(obj):
    """
    Select and make the object active in the scene

    Args:
        obj: object.
    """
    deselect_all_objects()
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj


def deselect_all_objects():
    """
    Similar to bpy.ops.object.select_all(action="DESELECT")
    """
    for obj in bpy.data.objects:
        obj.select_set(False)


def render_animation():
    """start rendering the animation
    same as Menu > Render > Render Animation"""
    bpy.ops.render.render(animation=True)


def app_version_is_or_greater_than(major: int, minor: int = 0, subversion: int = 0) -> bool:
    """The current version of Blender is equal to or
    greater than the passed in major.minor.subversion
    """
    return bpy.app.version >= (major, minor, subversion)


def app_version_less_than(major: int, minor: int = 0, subversion: int = 0) -> bool:
    """The current version of Blender is less than
    the passed in major.minor.subversion
    """
    return bpy.app.version < (major, minor, subversion)


@contextlib.contextmanager
def edit_mode():
    """
    A context manager for toggling the edit_mode

    Usage:
    with edit_mode():
        # do mesh editing
    """
    # enter edit mode
    bpy.ops.object.editmode_toggle()

    yield  # return out of the function in edit_mode

    # when leaving the context manager scope - exit edit_mode
    bpy.ops.object.editmode_toggle()


def purge_orphans():
    """
    Remove all orphan data blocks

    see this from more info:
    https://youtu.be/3rNqVPtbhzc?t=149
    """
    if bpy.app.version >= (3, 0, 0):
        # run this only for Blender versions 3.0 and higher
        bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
    else:
        # run this only for Blender versions lower than 3.0
        # call purge_orphans() recursively until there are no more orphan data blocks to purge
        result = bpy.ops.outliner.orphans_purge()
        if result.pop() != "CANCELLED":
            purge_orphans()


def clean_scene():
    """
    Removing all of the objects, collection, materials, particles,
    textures, images, curves, meshes, actions, nodes, and worlds from the scene

    Checkout this video explanation with example

    "How to clean the scene with Python in Blender (with examples)"
    https://youtu.be/3rNqVPtbhzc
    """
    # make sure the active object is not in Edit Mode
    if bpy.context.active_object and bpy.context.active_object.mode == "EDIT":
        bpy.ops.object.editmode_toggle()

    # make sure non of the objects are hidden from the viewport, selection, or disabled
    for obj in bpy.data.objects:
        obj.hide_set(False)
        obj.hide_select = False
        obj.hide_viewport = False

    # select all the object and delete them (just like pressing A + X + D in the viewport)
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()

    # find all the collections and remove them
    collection_names = [col.name for col in bpy.data.collections]
    for name in collection_names:
        bpy.data.collections.remove(bpy.data.collections[name])

    # in the case when you modify the world shader
    # delete and recreate the world object
    world_names = [world.name for world in bpy.data.worlds]
    for name in world_names:
        bpy.data.worlds.remove(bpy.data.worlds[name])
    # create a new world data block
    bpy.ops.world.new()
    bpy.context.scene.world = bpy.data.worlds["World"]

    purge_orphans()


def clean_scene_experimental():
    """
    An alternative clean scene function that just deletes
    the whole scene and creates a new one.

    Note: This might crash Blender! (hence experimental in the name)
    Proceed at your own risk!
    """

    # rename the current scene, so the new scene won't have a Scene.001
    old_scene_name = "to_delete"
    bpy.context.window.scene.name = old_scene_name

    # create a new scene (the name should be just "Scene")
    bpy.ops.scene.new()

    # remove the old scene
    bpy.data.scenes.remove(bpy.data.scenes[old_scene_name])

    # create a new world data block
    bpy.ops.world.new()
    bpy.context.scene.world = bpy.data.worlds["World"]

    purge_orphans()


def remove_libraries() -> None:
    """
    Remove libraries that were linked into the Blend file
    """
    bpy.data.batch_remove(bpy.data.libraries)


def render_animation():
    """
    Renders the animation in the currently active scene
    """
    bpy.ops.render.render(animation=True)


def render_image(write_still=False):
    """
    Renders an image in the currently active scene at the current frame

    Args:
        write_still: write the rendered image to disk. Defaults to False.
    """
    bpy.ops.render.render(write_still=write_still)


def parent(child_obj, parent_obj, keep_transform=False):
    """
    Parent the child object to the parent object

    Args:
        child_obj: child object that will be parented.
        parent_obj: parent object that will be parented to.
        keep_transform: keep the transform of the child object. Defaults to False.
    """
    make_active(child_obj)
    child_obj.parent = parent_obj
    if keep_transform:
        child_obj.matrix_parent_inverse = parent_obj.matrix_world.inverted()


def duplicate_object(obj=None, linked=False):
    """
    Duplicate object

    Args:
        obj: source object that will be duplicated.
        linked: link duplicated object to target source.
    """
    if obj is None:
        obj = active_object()

    deselect_all_objects()
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj

    bpy.ops.object.duplicate(linked=linked)
    duplicate_obj = active_object()

    return duplicate_obj


def apply_scale():
    bpy.ops.object.transform_apply(scale=True)


def apply_location():
    bpy.ops.object.transform_apply(location=True)


def apply_rotation():
    bpy.ops.object.transform_apply(rotation=True)
