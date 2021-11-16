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

bl_info = {
    "name": "Save Render Presets",
    "author": "Rombout Versluijs, Daniel Engler",
    "version": (0, 0, 3),
    "blender": (2, 93, 0),
    "location": "Properties > Render",
    "description": "Saves presets of all settign render tab",
    "tracker_url": "https://github.com/schroef/Save-Render-Presets/issues",
    "wiki_url": "https://github.com/schroef/Save-Render-Presets",
    "category": "Render",
}


import bpy
from .workbench_presets import *
from .cycles_presets import *
from .eevee_presets import *



def cycles_presets_menu(self, context):
    scene = context.scene
    layout = self.layout
    layout.use_property_split = True
    layout.use_property_decorate = False
    # layout = self.layout

    # row = layout.row(align=True)
    # row.label(text="Render Preset")
    # row = layout.split()

    layout.separator()
    row = layout.row(align=True)
    row.alignment = 'RIGHT'
    row.label(text="Render Presets")
    # row.label(text="Render Presets")
    # row.alignment = 'EXPAND'
    # self.draw_framerate(layout, col, rd)
    # print(context.engine)
    if(context.engine == 'BLENDER_WORKBENCH'):
        row.menu("WORKBENCH_MT_render_presets",text=bpy.types.WORKBENCH_MT_render_presets.bl_label)
        row.operator("render.workbench_render_preset_add", text="", icon="ADD")
        row.operator("render.workbench_render_preset_add", text="", icon="REMOVE").remove_active = True
    if(context.engine == 'CYCLES'):
        row.menu("CYCLES_MT_render_presets",text=bpy.types.CYCLES_MT_render_presets.bl_label)
        row.operator(CYCLES_OT_AddCyclesPreset.bl_idname, text="", icon="ADD")
        row.operator(CYCLES_AddPresetRender.bl_idname, text="", icon="REMOVE").remove_active = True
    if(context.engine == 'BLENDER_EEVEE'):
        row.menu("EEVEE_MT_render_presets",text=bpy.types.EEVEE_MT_render_presets.bl_label)
        row.operator(EEVEE_OT_AddEeveePreset.bl_idname, text="", icon="ADD")
        row.operator(EEVEE_AddPresetRender.bl_idname, text="", icon="REMOVE").remove_active = True


classes = (
    WORKBENCH_MT_render_presets,
    WORKBENCH_AddPresetRender,
    CYCLES_MT_render_presets,
    CYCLES_AddPresetRender,
    CYCLES_OT_AddCyclesPreset,
    EEVEE_MT_render_presets,
    EEVEE_AddPresetRender,
    EEVEE_OT_AddEeveePreset,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
    bpy.types.RENDER_PT_context.append(cycles_presets_menu)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
