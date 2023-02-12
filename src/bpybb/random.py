"""
This module contains utilities for working with random number generation.
"""

import math
import random
import time

import bpy
import mathutils

from bpybb.utils import active_object, apply_rotation


def time_seed() -> float:
    """
    Sets the random seed based on the time
    and copies the seed into the clipboard
    """
    seed = time.time()
    print(f"seed: {seed}")
    random.seed(seed)

    bpy.context.window_manager.clipboard = str(seed)

    return seed


def get_random_rotation() -> mathutils.Euler:
    """Returns a random Euler rotation on X, Y, Z"""
    x = math.radians(random.uniform(0, 360))
    y = math.radians(random.uniform(0, 360))
    z = math.radians(random.uniform(0, 360))
    return mathutils.Euler((x, y, z))


def apply_random_rotation() -> None:
    """
    Applies a random rotation on X, Y, Z for the currently active object
    """
    obj = active_object()

    obj.rotation_euler = get_random_rotation()

    apply_rotation()
