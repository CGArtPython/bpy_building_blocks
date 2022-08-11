"""
This module contains utilities for working with Blender add-ons.
"""

import addon_utils


def enable_addon(addon_module_name):
    """
    Checkout this video explanation with example

    "How to enable add-ons with Python in Blender (with examples)"
    https://youtu.be/HnrInoBWT6Q
    """
    loaded_default, loaded_state = addon_utils.check(addon_module_name)
    if not loaded_state:
        addon_utils.enable(addon_module_name)


def enable_extra_curves():
    """
    enable Add Curve Extra Objects addon
    https://docs.blender.org/manual/en/3.0/addons/add_curve/extra_objects.html
    """
    enable_addon(addon_module_name="add_curve_extra_objects")


def enable_extra_meshes():
    """
    enable Add Mesh Extra Objects addon
    https://docs.blender.org/manual/en/3.0/addons/add_mesh/mesh_extra_objects.html
    """
    enable_addon(addon_module_name="add_mesh_extra_objects")


def enable_ant_landscape():
    """
    enable ANT Landscape addon
    https://docs.blender.org/manual/en/3.0/addons/add_mesh/ant_landscape.html
    """
    enable_addon(addon_module_name="ant_landscape")


def enable_mod_tools():
    """
    enable Modifier Tools addon
    https://docs.blender.org/manual/en/3.0/addons/add_mesh/ant_landscape.html
    """
    enable_addon(addon_module_name="space_view3d_modifier_tools")


def enable_import_images_as_planes():
    """
    enable Images as Planes addon
    https://docs.blender.org/manual/en/3.0/addons/import_export/images_as_planes.html
    """
    enable_addon(addon_module_name="io_import_images_as_planes")


def enable_pointcache_pc2():
    """
    enable Pointcache (pc2) addon
    https://docs.blender.org/manual/en/3.0/addons/import_export/pc2.html
    """
    enable_addon(addon_module_name="io_export_pc2")


def enable_animation_animall():
    """
    enable Animall addon
    https://docs.blender.org/manual/en/dev/addons/animation/animall.html
    """
    enable_addon(addon_module_name="animation_animall")
