import time
import random

import bpy


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
