# Summary

A collection of helper functions and code used for speeding up Blender 3D Python script development.

Checkout project examples [YouTube: Art with a Python script](https://www.youtube.com/watch?v=rIhXHSdMWmc&list=PLB8-FQgROBmm-2f6Vyos6rbnjZeEScrX1)

Important: This package assumes you are using [Blender's](https://www.blender.org/) embedded Python interpreter. 

# Installation

## Installation Walkthrough Video 

[YouTube: How to install the bpy Building Blocks Python package](https://www.youtube.com/watch?v=_irmuKXjhS0)

## From the command line via pip (into Blender's embedded Python interpreter)

---

### on Windows

**Important:**
Make sure the `site-packages` folder of Blender's embedded Python interpreter is `writable`.
_See video ^ if you are not sure how to do that_
If you won't do this the package will be installed into another folder outside of Blender's embedded Python interpreter.
And you will see this warning: `Defaulting to user installation because normal site-packages is not writeable`

Run the pip install:
* `Blender <VERSION>/<VERSION>/python/bin/python.exe -m pip install bpy-building-blocks`

Example:
* `> cd C:\Program Files\Blender Foundation\Blender 3.2\3.2\python\bin `
* `> .\python.exe -m pip install bpy-building-blocks`

---

### on macOS

**Important:**
Make sure pip is available.

Run `ensurepip`
* `/Applications/Blender.app/Contents/Resources/<VERSION>/python/bin/python -m ensurepip`

Run the pip install:
* `/Applications/Blender.app/Contents/Resources/<VERSION>/python/bin/python -m pip install bpy-building-blocks`

---

### on Linux

**Important:**
Make sure pip is available.

Run `ensurepip`
* `~/<INSTALL LOCATION OF BLENDER>/<VERSION>/python/bin/python -m ensurepip`

Run the pip install:
* `~/<INSTALL LOCATION OF BLENDER>/<VERSION>/python/bin/python -m pip install bpy-building-blocks`

---

## Via Blender Add-on

[bpy_building_blocks_addon on github](https://github.com/CGArtPython/bpy_building_blocks_addon/releases)

See video for details [YouTube: How to install the bpy Building Blocks Python package](https://www.youtube.com/watch?v=_irmuKXjhS0)

# Package Contents

## Utilities

* bpybb.utils.active_object() - Get a references to the currently active object 
* bpybb.utils.clean_scene() - Removing all of the objects, collection, materials, particles, textures, images, curves, meshes, actions, nodes, and worlds from the scene; Checkout this video explanation with example ["How to clean the scene with Python in Blender (with examples)"](https://youtu.be/3rNqVPtbhzc)
* bpybb.utils.purge_orphans() - Remove all orphan data blocks; see this from more info: https://youtu.be/3rNqVPtbhzc?t=149
* bpybb.utils.edit_mode() - A context manager to get into and out of edit mode
* bpybb.utils.make_active(obj) - Make the passed in object active
* bpybb.utils.parent(child_obj, parent_obj, keep_transform=False) - Parent one object to another
* bpybb.utils.duplicate_object(obj=None, linked=False)
* bpybb.utils.render_animation() - Renders the animation in the currently active scene
* bpybb.utils.render_image(write_still=False) - Renders the currently active scene
* bpybb.utils.remove_libraries() - Remove libraries that were linked into the Blend file
* bpybb.utils.deselect_all_objects() - Similar to bpy.ops.object.select_all(action="DESELECT")

## Color Utilities

* bpybb.color.convert_srgb_to_linear_rgb(srgb_color_component) - Converting from sRGB to Linear RGB based on [sRGB to CIE XYZ](https://en.wikipedia.org/wiki/SRGB#From_sRGB_to_CIE_XYZ)
* bpybb.color.hex_color_to_rgb(hex_color) - Converting from a color in the form of a [hex triplet string](en.wikipedia.org/wiki/Web_colors#Hex_triplet) to a Linear RGB (Supports: "#RRGGBB" or "RRGGBB")
* bpybb.color.hex_color_to_rgba(hex_color, alpha=1.0) - Converting from a color in the form of a hex triplet string to a Linear RGB (Supports: "#RRGGBB" or "RRGGBB") with an Alpha value

## Add-on Utilities

* bpybb.addon.enable_addon(addon_module_name) - enables a given addon; Checkout this video explanation with example ["How to enable add-ons with Python in Blender (with examples)"](https://youtu.be/HnrInoBWT6Q)
* bpybb.addon.enable_animation_animall() - enable [Animall addon](https://docs.blender.org/manual/en/dev/addons/animation/animall.html)
* bpybb.addon.enable_ant_landscape() - enable [ANT Landscape addon](https://docs.blender.org/manual/en/3.0/addons/add_mesh/ant_landscape.html)
* bpybb.addon.enable_extra_curves() - enable [Add Curve Extra Objects addon](https://docs.blender.org/manual/en/3.0/addons/add_curve/extra_objects.html)
* bpybb.addon.enable_extra_meshes() - enable [Add Mesh Extra Objects addon](https://docs.blender.org/manual/en/3.0/addons/add_mesh/mesh_extra_objects.html)
* bpybb.addon.enable_import_images_as_planes() - enable [Images as Planes addon](https://docs.blender.org/manual/en/3.0/addons/import_export/images_as_planes.html)
* bpybb.addon.enable_mod_tools() - enable [Modifier Tools addon](https://docs.blender.org/manual/en/3.0/addons/add_mesh/ant_landscape.html)
* bpybb.addon.enable_pointcache_pc2() - enable [Pointcache (pc2) addon](https://docs.blender.org/manual/en/3.0/addons/import_export/pc2.html)

## Collection Utilities

* bpybb.collection.create_collection(col_name) - creates a [Blender Scene Collection](https://docs.blender.org/manual/en/latest/scene_layout/collections/collections.html)
* bpybb.collection.create_collection(collection_name: str, location: mathutils.Vector, rotation_euler: Optional[mathutils.Euler] = None, base_collection: Optional[bpy_types.Collection] = None) -> bpy_types.Object - creates an instance of a collection

## HDRI Utilities

* bpybb.hdri.apply_hdri(path_to_image, bg_color, hdri_light_strength, bg_strength) - creates a HDRI setup based on a technique from a [FlippedNormals tutorial](https://www.youtube.com/watch?v=dbAWTNCJVEs)

## Material Utilities

* bpybb.material.apply_material(material) - apply a material to the currently active object.
* bpybb.material.make_color_ramp_from_color_list(colors, color_ramp_node) - creates new sliders on a Color Ramp Node and applies the list of colors on each slider

## Mesh Utilities

* bpybb.mesh.get_vert_coordinates_list(obj) - get a list of vertex coordinates for a given object
* bpybb.mesh.subdivide() - subdivide the current active object

## Random Utilities

* bpybb.random.time_seed() - Sets the random seed based on the time and copies the seed into the clipboard
* bpybb.random.get_random_rotation() - Returns a random Euler rotation on X, Y, Z

## Object Utilities

* bpybb.object.add_empty(name=None) - Add an Empty object into the scene
* bpybb.object.apply_location() - Applies the location of the current object
* bpybb.object.rotate_object(axis: int, degrees: float) - Rotate the active object about a given axis
* bpybb.object.track_empty(obj) - Adds an Empty object and adds a To Track Constraint on the passed in object to track the Empty
* bpybb.object.add_bezier_circle(radius: float = 1.0, bevel_depth: float = 0.0, resolution_u: int = 12, extrude: float = 0.0) - Adds a Bezier circle curve into the scene.
* bpybb.object.add_round_cube(radius: float = 1.0) - Adds a Round Cube into the scene.
* bpybb.object.add_subdivided_round_cube(radius: float = 1.0) - Adds a Round Cube into the scene and applies a Subdivision modifier.
* join_objects(objects: list[bpy_types.Object]) -> bpy_types.Object - Joins the provided objects into one object

## Animation Utilities

* bpybb.animate.set_fcurve_extrapolation_to_linear(obj=None) - loops over all the fcurves of an action and sets the extrapolation to "LINEAR"
* bpybb.animate.set_fcurve_interpolation_to_linear(obj=None) - loops over all the fcurve key frame points of an action and sets the interpolation to "LINEAR"
* bpybb.animate.animate_360_rotation(axis_index, last_frame, obj=None, clockwise=False, linear=True, start_frame=1) - animates the 360 rotation of an object about the given axis
* bpybb.animate.animate_rotation(angle, axis_index, last_frame, obj=None, clockwise=False, linear=True, start_frame=1) - animates the rotation of an object about the given axis
* bpybb.animate.create_data_animation_loop(obj, data_path, start_value, mid_value, start_frame, loop_length, linear_extrapolation=True) - make a data property loop
* bpybb.animate.animate_up_n_down_bob(start_value: mathutils.Vector, mid_value: mathutils.Vector, obj: bpy_types.Object = None, loop_length: int = 90, start_frame: int = random.randint(0, 60)) - animate the up and down bobbing motion of an object
* bpybb.animate.add_fcruve_cycles_modifier(obj: bpy_types.Object = None) - Apply a cycles modifier to all the fcurve animation data of an object.

## Modifier Utilities

* bpybb.modifier.add_displace_modifier(name: str, texture_type: str, empty_obj: bpy_types.Object = None) - Add a displace modifier and a texture to the currently active object.

## Output Utilities

* bpybb.output.set_1080p_render_res() - Set the resolution of the rendered image to 1080p
* bpybb.output.set_1080px_square_render_res() - Set the resolution of the rendered image to 1080 by 1080 pixels
* bpybb.output.set_1440px_square_render_res() - Set the resolution of the rendered image to 1440 by 1440 pixels
* bpybb.output.set_2048px_square_render_res() - Set the resolution of the rendered image to 2048 by 2048 pixels
* bpybb.output.set_2k_render_res() - Set the resolution of the rendered image to 2K
* bpybb.output.set_4096px_square_render_res() - Set the resolution of the rendered image to 4096 by 4096 pixels
* bpybb.output.set_4k_render_res() - Set the resolution of the rendered image to 4K
* bpybb.output.set_720px_square_render_res() - Set the resolution of the rendered image to 720 by 720 pixels
* bpybb.output.set_instagram_portrait_render_res() - Set the resolution of the rendered image to 1080x1350
* bpybb.output.set_instagram_square_render_res() - Set the resolution of the rendered image to 1080x1080
* bpybb.output.set_square_render_res(pixels) - Set the resolution of the rendered image to a square
* bpybb.output.set_twitter_landscape_render_res() - Set the resolution of the rendered image to 1280x720 from Twitter's Media Best Practices ref: https://developer.twitter.com/en/docs/twitter-api/v1/media/upload-media/uploading-media/media-best-practices
* bpybb.output.set_twitter_square_render_res() - Set the resolution of the rendered image to 720x720 from Twitter's Media Best Practices ref: https://developer.twitter.com/en/docs/twitter-api/v1/media/upload-media/uploading-media/media-best-practices
* bpybb.output.set_wqhd_render_res() - Set the resolution of the rendered image to 2560x1440 (QHD)

## World Shader Utilities

* bpybb.world_shader.set_up_world_sun_light() - Set up the lighing in a scene using the ShaderNodeTexSky world shader node