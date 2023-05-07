"""
This module contains utilities working with Blender collections.
"""

import logging

from typing import Optional

import bpy
import bpy_types
import mathutils

from bpybb.utils import active_object, deselect_all_objects


def create_collection(collection_name: str) -> bpy_types.Collection:
    deselect_all_objects()

    bpy.ops.collection.create(name=collection_name)
    collection = bpy.data.collections[collection_name]

    bpy.context.scene.collection.children.link(collection)

    return collection


def add_to_collection(collection_name: str, obj: Optional[bpy_types.Object] = None, base_collection: Optional[bpy_types.Collection] = None) -> None:
    """
    Adds a given object to a collection with collection_name
    """
    if obj is None:
        obj = active_object()

    if base_collection is None:
        base_collection = bpy.context.scene.collection

    collection = bpy.data.collections.get(collection_name)
    if collection is None:
        logging.error("couldn't find a collection with the name '%s' ", collection_name)
        return
    collection.objects.link(obj)

    base_collection.objects.unlink(obj)


def make_instance_of_collection(
    collection_name: str, location: mathutils.Vector, rotation_euler: Optional[mathutils.Euler] = None, base_collection: Optional[bpy_types.Collection] = None
) -> bpy_types.Object:
    source_collection = bpy.data.collections.get(collection_name)
    if source_collection is None:
        logging.error("couldn't find a collection with the name '%s' ", collection_name)
        return

    if base_collection is None:
        base_collection = bpy.context.scene.collection

    new_name = f"{collection_name}.instance.{str(location)}"
    collection_instance = bpy.data.objects.new(name=new_name, object_data=None)
    collection_instance.location = location
    collection_instance.instance_type = "COLLECTION"
    collection_instance.instance_collection = source_collection

    base_collection.objects.link(collection_instance)

    if rotation_euler:
        collection_instance.rotation_euler = rotation_euler

    return collection_instance
