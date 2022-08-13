"""
This module contains utilities for working with random number generation.
"""

import math
import random
import time

import bpy


from bpybb.utils import active_object, apply_rotation


def time_seed():
    """
    Sets the random seed based on the time
    and copies the seed into the clipboard
    """
    seed = time.time()
    print(f"seed: {seed}")
    random.seed(seed)

    bpy.context.window_manager.clipboard = str(seed)

    return seed


def apply_random_rotation():
    """
    Applies a random rotation on X, Y, Z for the currently active object
    """
    obj = active_object()

    obj.rotation_euler.x = math.radians(random.uniform(0, 360))
    obj.rotation_euler.y = math.radians(random.uniform(0, 360))
    obj.rotation_euler.z = math.radians(random.uniform(0, 360))

    apply_rotation()
