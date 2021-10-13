# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

"""
Save-Render-Presets

Save your Color Management options as presets, for easy re-use.

It will pretty much every option in the Color Management panel, such as
the look, color settings, and so on. Except the curve points (have to
figure out how to do that nicely), good news is that in Blender 2.69+ you
can now copy/paste curves.
"""

bl_info = {
    "name": "Save Render Presets",
    "author": "Rombout Versluijs",
    "version": (0, 0, 1),
    "blender": (2, 93, 0),
    "location": "Properties > Render",
    "description": "Saves presets of all settign render tab",
    "warning": "https://github.com/schroef/Save-Render-Presets/issues",
    "doc_url": "https://github.com/schroef/Save-Render-Presets",
    "category": "Render",
}


import bpy
import inspect
from bl_operators.presets import AddPresetBase
from bpy.types import Panel, Operator, StringProperty
from mathutils import Color
# from bl_ui.utils import PresetPanel

# PRESET_SUBDIR = "eevee_presets"
# EXCLUDE_LIST = ["__", "bl_rna", "gi_cache_info", "rna_type"]
# EEVEE_KEY_PREFIX = "eevee"
# PRESET_HEAD = ["import bpy","eevee = bpy.context.scene.eevee","render = bpy.context.scene.render"]

# Preset meanu header
# class CYCLES_PT_add_render_presets(PresetPanel, Panel):
#     bl_label = "Render Presets"
#     preset_subdir = "cycles/rendering"
#     preset_operator = "script.execute_preset"
#     preset_add_operator = "render.cycles_render_preset_add"
#     COMPAT_ENGINES = {'CYCLES'}


class WORKBENCH_MT_render_presets(bpy.types.Menu):
    """List of Workbench Render presets"""
    bl_label = "Workbench Render Presets"
    preset_subdir = "render-presets/workbench"
    preset_operator = "script.execute_preset"
    draw = bpy.types.Menu.draw_preset


class WORKBENCH_AddPresetRender(AddPresetBase, Operator):
    '''Add a Render Preset'''
    bl_idname = "render.workbench_render_preset_add"
    bl_label = "Add Render Preset"
    preset_menu = "WORKBENCH_MT_render_presets"

    preset_defines = [
        "context = bpy.context",
        "scene = context.scene",
        "render = scene.render",
        "shading = bpy.types.VIEW3D_PT_shading.get_shading(context)",
    ]

    preset_values = [
        # Normals
        "scene.render.use_high_quality_normals",
        # Grease Pencil
        "scene.grease_pencil_settings.antialias_threshold",
        # Sampling
        "scene.display.render_aa",
        "scene.display.viewport_aa",
        # Lighting
        "shading.color_type",
        # Color
        "shading.light",
        "shading.studio_light",
        # Options
        "shading.show_backface_culling",
        "shading.show_xray",
        "shading.show_shadows",
        "shading.show_cavity",
        "shading.use_dof",
        "shading.show_object_outline",
        "shading.object_outline_color",
        "shading.show_specular_highlight",
        # Film
        "scene.render.film_transparent",
        # Simplify
        "render.use_simplify",
        "render.simplify_subdivision",
        "render.simplify_child_particles",
        "render.simplify_subdivision_render",
        "render.simplify_child_particles_render",
        # GreasePencil
        "render.simplify_gpencil",
        "render.simplify_gpencil_onplay",
        "render.simplify_gpencil_view_fill",
        "render.simplify_gpencil_modifier",
        "render.simplify_gpencil_shader_fx",
        "render.simplify_gpencil_tint",
        "render.simplify_gpencil_antialiasing",
    ]

    preset_subdir = "render-presets/workbench"


class CYCLES_MT_render_presets(bpy.types.Menu):
    """List of Cycles Render presets"""
    bl_label = "Cycles Render Presets"
    preset_subdir = "render-presets/cycles"
    preset_operator = "script.execute_preset"
    draw = bpy.types.Menu.draw_preset


class CYCLES_AddPresetRender(AddPresetBase, Operator):
    '''Add a Render Preset'''
    bl_idname = "render.cycles_render_preset_add"
    bl_label = "Add Render Preset"
    preset_menu = "CYCLES_MT_render_presets"

    preset_defines = [
        "context = bpy.context",
        "scene = context.scene",
        "render = scene.render",
        "cycles = scene.cycles",
        "world = scene.world",
        "cycles_curves = scene.cycles_curves",
        "viewlayers = scene.view_layers",
    ]

    preset_values = [
        # Feature Set
        "cycles.feature_set",
        # Device
        "cycles.device",
        # OpenShadingLanguage
        "cycles.shading_system",

        # Grease Pencil
        "scene.grease_pencil_settings.antialias_threshold",

        # Samples Pathtracing
        "cycles.samples",
        "cycles.preview_samples",
        "cycles.aa_samples",
        # Not sure how todo this one
        # "viewlayers.samples",
        
        # Samples Branched Pathtracing
        # Subd Samples
        "cycles.diffuse_samples",
        "cycles.glossy_samples",
        "cycles.transmission_samples",
        "cycles.ao_samples",
        "cycles.mesh_light_samples",
        "cycles.subsurface_samples",
        "cycles.volume_samples",

        # Adaptive
        "cycles.use_adaptive_sampling",
        "cycles.adaptive_threshold",
        "cycles.adaptive_min_samples",
        # Denoise bl293
        "cycles.use_denoising",
        "cycles.denoiser",
        "cycles.use_preview_denoising",
        "cycles.preview_denoiser",
        "cycles.preview_denoising_start_sample",
        "cycles.preview_denoising_input_passes",
        # Advanced
        "cycles.seed",
        "cycles.use_animated_seed",
        "cycles.sampling_pattern",
        "cycles.use_square_samples",
        "cycles.min_light_bounces",
        "cycles.min_transparent_bounces",
        "cycles.light_sampling_threshold",

        "cycles.preview_aa_samples",
        "cycles.progressive",
        
        # Light bounces
        # Max
        "cycles.max_bounces",
        "cycles.diffuse_bounces",
        "cycles.glossy_bounces",
        "cycles.transparent_max_bounces",
        "cycles.transmission_bounces",
        "cycles.volume_bounces",
        # Clamping
        "cycles.sample_clamp_direct",
        "cycles.sample_clamp_indirect",
        # Caustics
        "cycles.blur_glossy",
        "cycles.caustics_reflective",
        "cycles.caustics_refractive",
        # ???
        "cycles.sample_all_lights_direct",
        "cycles.sample_all_lights_indirect",
        # Fast GI Approximation
        "cycles.use_fast_gi",
        "cycles.ao_bounces",
        "cycles.ao_bounces_render",
        "world.light_settings.ao_factor",
        "world.light_settings.distance",
        
        # Volumes
        "cycles.volume_step_rate",
        "cycles.volume_preview_step_rate",
        "cycles.volume_max_steps",
        
        # Hair bl283
        # "cycles_curves.use_curves",
        # "cycles_curves.cull_backfacing",
        # "cycles_curves.primitive",
        # "cycles_curves.resolution",
        # Hair bl293
        "cycles_curves.shape",
        "cycles_curves.subdivisions",

        # Simplify
        # preview
        "render.use_simplify",
        "render.simplify_subdivision",
        "cycles.texture_limit",
        "cycles.texture_limit",
        "cycles.ao_bounces",
        # Render
        "render.simplify_subdivision_render",
        "render.simplify_child_particles_render",
        "cycles.texture_limit_render",
        "cycles.ao_bounces_render",
        # Culling
        "cycles.use_camera_cull",
        "cycles.camera_cull_margin",
        "cycles.use_distance_cull",
        "cycles.use_distance_cull",
        "cycles.distance_cull_margin",
        # GreasePencil Simplify
        "render.simplify_gpencil",
        "render.simplify_gpencil_onplay",
        "render.simplify_gpencil_view_fill",
        "render.simplify_gpencil_modifier",
        "render.simplify_gpencil_shader_fx",
        "render.simplify_gpencil_tint",
        "render.simplify_gpencil_antialiasing",

        # Motion Blur
        "render.use_motion_blur",

        # Film
        "cycles.film_exposure",
        # Film bl293
        "cycles.pixel_filter_type",
        "render.film_transparent",
        "cycles.film_transparent_glass",
        "cycles.film_transparent_roughness",
        
        # Performance
        # Threads
        "render.threads_mode",
        "render.threads",
        # Tiles
        "render.tile_x",
        "render.tile_y",
        "cycles.tile_order",
        "cycles.use_progressive_refine",
        # Accelaration Structure
        "cycles.debug_use_spatial_splits",
        "cycles.debug_use_hair_bvh",
        "cycles.debug_bvh_time_steps",
        # Final Render
        "render.use_save_buffers",
        "render.use_persistent_data",
        # Viewport
        "render.preview_pixel_size",
        "cycles.preview_start_resolution",
        
        # Bake
        "render.use_bake_multires",
        "render.bake_type",
        # Output
        "render.bake.target",
        "render.bake_margin",
        "render.use_bake_clear",
        "render.use_bake_lores_mesh",
        # Influence
        "render.bake.use_pass_direct",
        "render.bake.use_pass_indirect",
        "render.bake.use_pass_diffuse",
        "render.bake.use_pass_color",
        "render.bake.use_pass_glossy",
        "render.bake.use_pass_transmission",
        "render.bake.use_pass_ambient_occlusion",
        "render.bake.use_pass_emit",
        "render.bake.normal_space",
        "render.bake.normal_r",
        "render.bake.normal_g",
        "render.bake.normal_b",

        # Selected to Active
        "render.bake.use_selected_to_active",
        "render.bake.use_cage",
        "render.bake.cage_extrusion",
        "render.bake.max_ray_distance",
        
        # Freestyle
        "render.use_freestyle",
        "render.line_thickness_mode",
        "render.line_thickness",
        
    ]

    preset_subdir = "render-presets/cycles"



class EEVEE_MT_render_presets(bpy.types.Menu):
    """List of Eevee Render presets"""
    bl_label = "EEVEE Render Presets"
    preset_subdir = "render-presets/eevee"
    preset_operator = "script.execute_preset"
    draw = bpy.types.Menu.draw_preset


class EEVEE_AddPresetRender(AddPresetBase, Operator):
    '''Add a EEVEE Render Preset'''
    bl_idname = "render.eevee_render_preset_add"
    bl_label = "Add EEVEE Render Preset"
    preset_menu = "EEVEE_MT_render_presets"

    preset_defines = [
        "eevee = bpy.context.scene.eevee",
        "render = bpy.context.scene.render",
    ]
   
    preset_values = [
        # Sampling
        "eevee.taa_render_samples",
        "eevee.taa_samples",
        "eevee.use_taa_reprojection",
        # AO
        "eevee.use_gtao",
        "eevee.gtao_distance",
        "eevee.gtao_factor",
        "eevee.gtao_quality",
        "eevee.use_gtao_bent_normals",
        "eevee.use_gtao_bounce",
        # Bloom
        "eevee.use_bloom",
        "eevee.bloom_threshold",
        "eevee.bloom_knee",
        "eevee.bloom_radius",
        "eevee.bloom_color",
        "eevee.bloom_intensity",
        "eevee.bloom_clamp",
        # DOF
        "eevee.bokeh_max_size",
        "eevee.bokeh_threshold",
        "eevee.bokeh_neighbor_max",
        "eevee.bokeh_denoise_fac",
        "eevee.use_bokeh_high_quality_slight_defocus",
        "eevee.use_bokeh_jittered",
        "eevee.bokeh_overblur",
        # SSS
        "eevee.sss_samples",
        "eevee.sss_jitter_threshold",
        # Screen Space Reflections
        "eevee.use_ssr",
        "eevee.use_ssr_refraction",
        "eevee.use_ssr_halfres",
        "eevee.ssr_quality",
        "eevee.ssr_max_roughness",
        "eevee.ssr_thickness",
        "eevee.ssr_border_fade",
        "eevee.ssr_firefly_fac",
        # Motion Blur
        # bl293
        "eevee.use_motion_blur",
        "eevee.motion_blur_position",
        "eevee.motion_blur_depth_scale",
        "eevee.motion_blur_max",
        "eevee.motion_blur_steps",
        # bl283
        # "eevee.motion_blur_samples",
        # "eevee.motion_blur_shutter",
        # Volumetrics
        "eevee.volumetric_start",
        "eevee.volumetric_end",
        "eevee.volumetric_tile_size",
        "eevee.volumetric_samples",
        "eevee.volumetric_sample_distribution",
        "eevee.use_volumetric_lights",
        "eevee.use_volumetric_shadows",
        "eevee.volumetric_light_clamp",
        "eevee.volumetric_shadow_samples",
        # Performance
        "render.use_high_quality_normals",
        # Hair
        "render.hair_type",
        "render.hair_subdiv",
        # Shadows
        "eevee.shadow_cascade_size",
        "eevee.shadow_cube_size",
        "eevee.use_shadow_high_bitdepth",
        "eevee.use_soft_shadows",
        "eevee.light_threshold",
        # Indirect Lighting
        "eevee.gi_auto_bake",
        "eevee.gi_cubemap_display_size",
        "eevee.gi_cubemap_resolution",
        "eevee.gi_diffuse_bounces",
        "eevee.gi_filter_quality",
        "eevee.gi_glossy_clamp",
        "eevee.gi_irradiance_display_size",
        "eevee.gi_irradiance_smoothing",
        "eevee.gi_show_cubemaps",
        "eevee.gi_show_irradiance",
        "eevee.gi_visibility_resolution",
        # Film
        "render.filter_size",
        "render.film_transparent",
        "eevee.use_overscan",
        "eevee.overscan_size",
        # Simplify
        "render.use_simplify",
        # preview
        "render.simplify_subdivision",
        "render.simplify_child_particles",
        "render.simplify_volumes",
        # Render
        "render.simplify_subdivision_render",
        "render.simplify_child_particles_render",
        # GreasePencil Simplify
        "render.simplify_gpencil",
        "render.simplify_gpencil_onplay",
        "render.simplify_gpencil_view_fill",
        "render.simplify_gpencil_modifier",
        "render.simplify_gpencil_shader_fx",
        "render.simplify_gpencil_tint",
        "render.simplify_gpencil_antialiasing",
        # Freestyle
        "render.use_freestyle",
        "render.line_thickness",

    ]

    preset_subdir = "render-presets/eevee"


def cycles_presets_menu(self, context):
    scene = context.scene
    layout = self.layout
    # if not context.engine == 'CYCLES':
    layout.use_property_split = True
    layout.use_property_decorate = False
    # layout = self.layout

    # row = layout.row(align=True)
    # row.label(text="Render Preset")
    # row = layout.split()

    layout.separator()
    # if not context.engine == 'CYCLES':
    row = layout.row(align=True)
    row.alignment = 'RIGHT'
    row.label(text="Render Presets")
    # row.alignment = 'EXPAND'
    # self.draw_framerate(layout, col, rd)
    # print(context.engine)
    if(context.engine == 'BLENDER_WORKBENCH'):
        row.menu("WORKBENCH_MT_render_presets",text=bpy.types.WORKBENCH_MT_render_presets.bl_label)
        row.operator("render.workbench_render_preset_add", text="", icon="ADD")
        row.operator("render.workbench_render_preset_add", text="", icon="REMOVE").remove_active = True
    if(context.engine == 'CYCLES'):
        row.menu("CYCLES_MT_render_presets",text=bpy.types.CYCLES_MT_render_presets.bl_label)
        row.operator("render.cycles_render_preset_add", text="", icon="ADD")
        row.operator("render.cycles_render_preset_add", text="", icon="REMOVE").remove_active = True
    if(context.engine == 'BLENDER_EEVEE'):
        row.menu("EEVEE_MT_render_presets",text=bpy.types.EEVEE_MT_render_presets.bl_label)
        row.operator("render.eevee_render_preset_add", text="", icon="ADD")
        row.operator("render.eevee_render_preset_add", text="", icon="REMOVE").remove_active = True


classes = (
    WORKBENCH_MT_render_presets,
    WORKBENCH_AddPresetRender,
    CYCLES_MT_render_presets,
    CYCLES_AddPresetRender,
    EEVEE_MT_render_presets,
    EEVEE_AddPresetRender,
    # CYCLES_PT_add_render_presets,
)




def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
    bpy.types.RENDER_PT_context.append(cycles_presets_menu)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    
    bpy.types.RENDER_PT_context.remove(cycles_presets_menu)


if __name__ == "__main__":
    register()
