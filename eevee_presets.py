import bpy
import inspect
from pathlib import Path
from bl_operators.presets import AddPresetBase
from bpy.props import BoolProperty, StringProperty
from bpy.types import Menu, Operator, Panel
from mathutils import Color

PRESET_SUBDIR = "render-presets/eevee"
EXCLUDE_LIST = ["__", "bl_rna", "gi_cache_info", "rna_type"]
EEVEE_KEY_PREFIX = "eevee"
PRESET_HEAD = """import bpy
eevee = bpy.context.scene.eevee
render = bpy.context.scene.render

"""


def get_eevee_values():
    pre_vals = {}
    eevee_settings_list = inspect.getmembers(bpy.context.scene.eevee)
    for elem in eevee_settings_list:
        key, value = elem
        if all(item not in key for item in EXCLUDE_LIST):
            if isinstance(value, Color):
                val = (value.r, value.g, value.b)
            elif isinstance(value, str):
                val = f"'{value}'"
            else:
                val = value
            pre_vals[f"{EEVEE_KEY_PREFIX}.{key}"] = val
    return pre_vals

# eevee_values = {}
#eevee_values[f"render.use_motion_blur"] = bpy.context.scene.render.use_motion_blur
#if self.film_transparent:
#    eevee_values[f"render.film_transparent"] = bpy.context.scene.render.film_transparent
# eevee_values.update(get_eevee_values())

# preset_lines = [PRESET_HEAD]
# for key, value in eevee_values.items():
#     line = f"{key} = {value}\n"
#     preset_lines.append(line)

# print(preset_lines)

class EEVEE_MT_render_presets(Menu):
    """List of Eevee Render presets"""
    bl_label = "EEVEE Render Presets"
    preset_subdir = PRESET_SUBDIR
    preset_operator = "script.execute_preset"
    draw = Menu.draw_preset


class EEVEE_AddPresetRender(AddPresetBase, Operator):
    '''Add a EEVEE Render Preset'''
    bl_idname = "render.eevee_preset_add_old"
    bl_label = "Add Eevee Render Preset OLD"
    preset_menu = "EEVEE_MT_render_presets"

    preset_defines = ["eevee = bpy.context.scene.eevee",
                      "render = bpy.context.scene.render"]

    preset_subdir = PRESET_SUBDIR


class EEVEE_OT_AddEeveePreset(Operator):
    bl_idname = "render.eevee_render_preset_add"
    bl_label = "Add Eevee Preset"

    preset_name: StringProperty(name="Name",
                                description="",
                                default="")

    # film_transparent: BoolProperty(name="Save Film Transparent",
    #                                     description="",
    #                                     default=True)

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        # layout.prop(self, "film_transparent")
        layout.prop(self, "preset_name")

    def execute(self, context):
        if self.preset_name == "":
            self.report({'INFO'}, "Preset needs a name!")
            return {'CANCELLED'}

        eevee_values = {}
        # eevee_values[f"render.use_motion_blur"] = bpy.context.scene.render.use_motion_blur
        # if self.film_transparent:
        #     eevee_values[f"render.film_transparent"] = bpy.context.scene.render.film_transparent
        eevee_values.update(get_eevee_values())

        preset_lines = [PRESET_HEAD]
        for key, value in eevee_values.items():
            line = f"{key} = {value}\n"
            preset_lines.append(line)

        user_path = Path(bpy.utils.resource_path('USER'))
        preset_path = user_path / Path(f"scripts/presets/{PRESET_SUBDIR}")

        try:
            if not preset_path.exists():
                preset_path.mkdir()
        except PermissionError as _:
            self.report(
                {'ERROR'}, f"PermissionError for '{preset_path}'")
            return {'CANCELLED'}
        except FileNotFoundError as _:
            self.report(
                {'ERROR'}, f"FileNotFoundError for '{preset_path}'")
            return {'CANCELLED'}

        preset_file_path = preset_path / Path(f"{self.preset_name}.py")

        with open(preset_file_path, 'w') as preset_file:
            preset_file.writelines(preset_lines)

        return {'FINISHED'}