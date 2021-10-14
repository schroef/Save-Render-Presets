import bpy
from bl_operators.presets import AddPresetBase
from bpy.types import Operator, Menu


class WORKBENCH_MT_render_presets(Menu):
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
