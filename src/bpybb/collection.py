"""
This module contains utilities working with Blender collections.
"""

from typing import Optional

import bpy
import bpy_types


def create_collection(col_name: str) -> bpy_types.Collection:
    bpy.ops.object.select_all(action="DESELECT")

    bpy.ops.collection.create(name=col_name)
    collection = bpy.data.collections[col_name]

    bpy.context.scene.collection.children.link(collection)

    return collection


def add_to_collection(col_name: str, obj: Optional[bpy_types.Object] = None, base_collection: Optional[bpy_types.Collection] = None) -> None:
    """
    Adds a given object to a collection with col_name
    """
    if obj is None:
        obj = bpy.context.active_object

    if base_collection is None:
        base_collection = bpy.context.scene.collection

    bpy.ops.object.collection_link(collection=col_name)

    base_collection.objects.unlink(obj)
