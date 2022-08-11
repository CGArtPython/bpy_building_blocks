"""
This module contains utilities for setting up the render resolution.
"""

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


def set_1440px_square_render_res():
    """
    Set the resolution of the rendered image to 1440 by 1440 pixels
    """
    set_square_render_res(pixels=1440)


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


def set_wqhd_render_res():
    """
    Set the resolution of the rendered image to 2560x1440 (QHD)
    """
    bpy.context.scene.render.resolution_x = 2560
    bpy.context.scene.render.resolution_y = 1440


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


def set_twitter_landscape_render_res():
    """
    Set the resolution of the rendered image to 1280x720
    from Twitter's Media Best Practices
    ref: https://developer.twitter.com/en/docs/twitter-api/v1/media/upload-media/uploading-media/media-best-practices
    """
    bpy.context.scene.render.resolution_x = 1280
    bpy.context.scene.render.resolution_y = 720


def set_twitter_square_render_res():
    """
    Set the resolution of the rendered image to 720x720
    from Twitter's Media Best Practices
    ref: https://developer.twitter.com/en/docs/twitter-api/v1/media/upload-media/uploading-media/media-best-practices
    """
    set_720px_square_render_res()


def set_instagram_portrait_render_res():
    """
    Set the resolution of the rendered image to 1080x1350
    """
    bpy.context.scene.render.resolution_x = 1080
    bpy.context.scene.render.resolution_y = 1350


def set_instagram_square_render_res():
    """
    Set the resolution of the rendered image to 1080x1080
    """
    set_1080px_square_render_res()
