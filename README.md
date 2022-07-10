# Summary

A collection of helper functions and code used for speeding up Blender 3D Python script development.

Important: This package assumes you are using [Blender's](https://www.blender.org/) the embedded Python interpreter. 

# Package Contents

## Utilities

* active_object() - Get a references to the currently active object 
* clean_scene() - Removing all of the objects, collection, materials, particles, textures, images, curves, meshes, actions, nodes, and worlds from the scene; Checkout this video explanation with example ["How to clean the scene with Python in Blender (with examples)"](https://youtu.be/3rNqVPtbhzc)
* purge_orphans() - Remove all orphan data blocks; see this from more info: https://youtu.be/3rNqVPtbhzc?t=149
* editmode() - A context manager to get into and out of edit mode
* make_active(obj) - Make the passed in object active
* parent(child_obj, parent_obj, keep_transform=False) - Parent one object to another
* render_animation() - Renders the animation in the currently active scene
* render_image(write_still=False) - Renders the currently active scene

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

## HDRI Utilities

* bpybb.hdri.apply_hdri(path_to_image, bg_color, hdri_light_strength, bg_strength) - creates a HDRI setup based on a technique from a [FlippedNormals tutorial](https://www.youtube.com/watch?v=dbAWTNCJVEs)

## Material Utilities

* bpybb.material.apply_material(material) - apply a material to the currently active object.
* bpybb.material.make_color_ramp_from_color_list(colors, color_ramp_node) - creates new sliders on a Color Ramp Node and applies the list of colors on each slider

## Mesh Utilities

* bpybb.mesh.get_vert_coordinates_list(obj) - get a list of vertex coordinates for a given object

## Random Utilities

* bpybb.random.time_seed() - Sets the random seed based on the time and copies the seed into the clipboard

## Object Utilities

* bpybb.object.add_empty(name=None) - Add an Empty object into the scene
* bpybb.object.apply_location() - Applies the location of the current object
* bpybb.object.track_empty(obj) - Adds an Empty object and adds a To Track Constraint on the passed in object to track the Empty

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
