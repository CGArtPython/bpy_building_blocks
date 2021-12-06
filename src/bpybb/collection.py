import bpy


def create_collection(col_name):
    bpy.ops.object.select_all(action="DESELECT")

    bpy.ops.collection.create(name=col_name)
    collection = bpy.data.collections[col_name]

    bpy.context.scene.collection.children.link(collection)

    return collection
