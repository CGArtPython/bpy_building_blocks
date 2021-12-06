import bpy


def set_square_render_res(pixels):
    """
    Set the resolution of the rendered image to a square
    """
    bpy.context.scene.render.resolution_x = pixels
    bpy.context.scene.render.resolution_y = pixels


def set_720px_square_render_res():
    """
    Set the resolution of the rendered image to 720 by 720 pixels
    """
    set_square_render_res(pixels=720)


def set_1080px_square_render_res():
    """
    Set the resolution of the rendered image to 1080 by 1080 pixels
    """
    set_square_render_res(pixels=1080)


def set_2048px_square_render_res():
    """
    Set the resolution of the rendered image to 2048 by 2048 pixels
    """
    set_square_render_res(pixels=2048)


def set_4096px_square_render_res():
    """
    Set the resolution of the rendered image to 4096 by 4096 pixels
    """
    set_square_render_res(pixels=4096)


def set_1080p_render_res():
    """
    Set the resolution of the rendered image to 1080p
    """
    bpy.context.scene.render.resolution_x = 1920
    bpy.context.scene.render.resolution_y = 1080


def set_2k_render_res():
    """
    Set the resolution of the rendered image to 2K
    """
    bpy.context.scene.render.resolution_x = 2048
    bpy.context.scene.render.resolution_y = 1080


def set_4k_render_res():
    """
    Set the resolution of the rendered image to 4K
    """
    bpy.context.scene.render.resolution_x = 4096
    bpy.context.scene.render.resolution_y = 2160
