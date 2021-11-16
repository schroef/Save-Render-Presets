import bpy
import inspect
from pathlib import Path
from bl_operators.presets import AddPresetBase
from bpy.props import BoolProperty, StringProperty
from bpy.types import Menu, Operator
from mathutils import Color

PRESET_SUBDIR = "render-presets/cycles"
EXCLUDE_LIST = ["__", "bl_rna", "gi_cache_info", "rna_type","_devices_update_callback","debug_","register","unregister"]
CYCLES_KEY_PREFIX = "cycles"
PRESET_HEAD = """import bpy
cycles = bpy.context.scene.cycles
render = bpy.context.scene.render

"""


def get_cycles_values():
    pre_vals = {}
    cycles_settings_list = inspect.getmembers(bpy.context.scene.cycles)
    for elem in cycles_settings_list:
        key, value = elem
        if all(item not in key for item in EXCLUDE_LIST):
            if isinstance(value, Color):
                val = (value.r, value.g, value.b)
            elif isinstance(value, str):
                val = f"'{value}'"
            else:
                val = value
            pre_vals[f"{CYCLES_KEY_PREFIX}.{key}"] = val
    return pre_vals

# cycles_values = {}
#cycles_values[f"render.use_motion_blur"] = bpy.context.scene.render.use_motion_blur
#if self.film_transparent:
#    cycles_values[f"render.film_transparent"] = bpy.context.scene.render.film_transparent
# cycles_values.update(get_cycles_values())

# preset_lines = [PRESET_HEAD]
# for key, value in cycles_values.items():
#     line = f"{key} = {value}\n"
#     preset_lines.append(line)

# print(preset_lines)


class CYCLES_MT_render_presets(Menu):
    """List of Cycles Render presets"""
    bl_label = "Cycles Render Presets"
    preset_subdir = PRESET_SUBDIR
    preset_operator = "script.execute_preset"
    draw = Menu.draw_preset


class CYCLES_AddPresetRender(AddPresetBase, Operator):
    '''Add a Render Preset'''
    bl_idname = "render.cycles_preset_add_old"
    bl_label = "Add Cycles Render Preset OLD"
    preset_menu = "CYCLES_MT_render_presets"

    preset_defines = ["cycles = bpy.context.scene.cycles",
                      "render = bpy.context.scene.render"]

    preset_subdir = PRESET_SUBDIR


class CYCLES_OT_AddCyclesPreset(Operator):
    bl_idname = "render.cycles_render_preset_add"
    bl_label = "Add Cycles Preset"
    
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

    @staticmethod
    def as_filename(name):  # could reuse for other presets

        # lazy init maketrans
        def maketrans_init():
            cls = AddPresetBase
            attr = "_as_filename_trans"

            trans = getattr(cls, attr, None)
            if trans is None:
                trans = str.maketrans({char: "_" for char in " !@#$%^&*(){}:\";'[]<>,.\\/?"})
                setattr(cls, attr, trans)
            return trans

        name = name.lower().strip()
        name = bpy.path.display_name_to_filepath(name)
        trans = maketrans_init()
        # Strip surrounding "_" as they are displayed as spaces.
        return name.translate(trans).strip("_")

    def execute(self, context):
        if self.preset_name == "":
            self.report({'INFO'}, "Preset needs a name!")
            return {'CANCELLED'}

        preset_menu_class = getattr(bpy.types, "CYCLES_MT_render_presets")
        cycles_values = {}
        # cycles_values[f"render.use_motion_blur"] = bpy.context.scene.render.use_motion_blur
        # if self.film_transparent:
        #     cycles_values[f"render.film_transparent"] = bpy.context.scene.render.film_transparent
        cycles_values.update(get_cycles_values())

        preset_lines = [PRESET_HEAD]
        for key, value in cycles_values.items():
            line = f"{key} = {value}\n"
            preset_lines.append(line)

        user_path = Path(bpy.utils.resource_path('USER'))
        preset_path = user_path / Path(f"scripts/presets/{PRESET_SUBDIR}")
        print(preset_path)
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

        filename = self.as_filename(self.preset_name)
        preset_file_path = preset_path / Path(f"{filename}.py")

        with open(preset_file_path, 'w') as preset_file:
            preset_file.writelines(preset_lines)
        
        # Set new Preset as active
        preset_menu_class.bl_label = bpy.path.display_name(filename)
        return {'FINISHED'}