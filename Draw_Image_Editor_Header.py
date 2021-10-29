import bpy
import pathlib
from . import Utility_Functions

#Show Engine

def draw_image_editor_header(self, context):

    layout = self.layout
    Image = context.space_data.image
    preferences = Utility_Functions.get_addon_preferences()

    row = layout.row(align=True)






    # if preferences.BTN_Open_Viewport:
    #     operator = row.operator("image_editor_extras.open_viewport", icon="VIEW3D")
    #     row.separator()

    if preferences.BTN_Render:
        # row2 = row.row(align=True)
        # row2.operator_context = "EXEC_DEFAULT"
        # operator = row2.operator("render.render", icon="RESTRICT_RENDER_OFF")

        row.operator("image_editor_extras.render", text="Render", icon="RESTRICT_RENDER_OFF")
    if preferences.BTN_Render_Engine:
        row.prop(context.scene.render, "engine", text="")

    if preferences.PROP_Render_Percentage:
        row.prop(context.scene.render, "resolution_percentage", text="Size")
    if preferences.PROP_Frame:
        row.prop(context.scene, "frame_current", text="Frame")

    if preferences.POPUP_Render_Settings:
        row.popover("IEH_PT_Render_Settings", text='', text_ctxt='', translate=True, icon='NONE', icon_value=0)

    if preferences.BTN_Open_Viewport:
        row.separator()
        operator = row.operator("image_editor_extras.open_viewport", icon="VIEW3D")
        row.separator()

        row = layout.row(align=True)

    if Image:
        if preferences.POPUP_Image_Swapper:
            row.separator()
            row.operator("image_editor_extras.swap_image", text="Swap", icon="UV_SYNC_SELECT")
            row.popover("IEH_PT_Swapper_Settings", text='', text_ctxt='', translate=True, icon='NONE', icon_value=0)
            row.separator()


    if Image:

        if Image.type == "RENDER_RESULT":

            if preferences.PROP_Slot_Changer:

                row = layout.row(align=True)
                operator = row.operator("image_editor_extras.next_slot", text="", icon="TRIA_LEFT")
                operator.direction = "BACK"
                row.prop(Image, "render_slot_changer", text="Slot")
                operator = row.operator("image_editor_extras.next_slot", text="", icon="TRIA_RIGHT")
                operator.direction = "NEXT"

            row = layout.row(align=True)
            row.separator()
            row.separator()
            # if preferences.BTN_Render:
            #     operator = row.operator("render.render", icon="RESTRICT_RENDER_OFF")
            # if preferences.POPUP_Render_Settings:
            #     row.popover("IEH_PT_Render_Settings", text='', text_ctxt='', translate=True, icon='NONE', icon_value=0)


            if preferences.POPUP_Render_Settings or preferences.BTN_Render:
                row = layout.row(align=True)

            if preferences.BTN_Pack:
                row.operator("image_editor_extras.pack_render", text="Pack", icon="PACKAGE")
            if preferences.BTN_Save:
                # row.operator("image.save_as", text="Save As", icon="FILE_TICK")
                row.operator("image_editor_extras.save_and_load", text="Save As and Load", icon="FILE_TICK")



        if not Image.type == "RENDER_RESULT":

            row = layout.row(align=True)
            if preferences.BTN_Pack:
                if not Image.packed_file:
                    if Image.type == "IMAGE":
                        row.operator("image.pack", text="Pack", icon="PACKAGE")

                else:
                    blend_file = pathlib.Path(bpy.data.filepath).stem

                    row.label(text="Packed", icon="PACKAGE")


                    col = row.column(align=True)
                    if not blend_file:
                        col.enabled = False
                        operator = col.operator("file.unpack_item", text="Unpack (Save Your Blend File)", icon="REMOVE")
                        operator.id_type = 19785
                        operator.id_name = Image.name

                    if blend_file:
                        operator = col.operator("file.unpack_item", icon="REMOVE")

                        operator.id_type = 19785
                        operator.id_name = Image.name


            if Image.type == "IMAGE":
                if preferences.BTN_Duplicate:
                    row.operator("image_editor_extras.duplicate_pack", text="Duplicate (Pack)", icon="DUPLICATE")
                    row.separator()

            if preferences.BTN_Save:
                if Image.is_dirty:
                    row.operator("image.save", text="Save*", icon="FILE_TICK")

                # row.operator("image.save_as", text="Save As", icon="FILE_TICK")
                row.operator("image_editor_extras.save_and_load", text="Save As and Load", icon="FILE_TICK")

            if preferences.BTN_Remove:
                row.separator()
                operator = row.operator("image_editor_extras.remove_image", text="", icon="TRASH")
                operator.image_name = Image.name

def draw_tool_settings_toogle(self, context):
    layout = self.layout
    preferences = Utility_Functions.get_addon_preferences()
    space = context.space_data

    if preferences.BTN_Mode_Changer:
        row = layout.row(align=True)

        if space.mode == "VIEW":
            row.operator("image_editor_extras.change_mode", text="View", icon="IMAGE_DATA", emboss=False).mode = "VIEW"
        else:
            row.operator("image_editor_extras.change_mode", text="View", icon="IMAGE_DATA", emboss=True).mode = "VIEW"

        if space.mode == "PAINT":
            row.operator("image_editor_extras.change_mode", text="Paint", icon="TPAINT_HLT", emboss=False).mode = "PAINT"
        else:
            row.operator("image_editor_extras.change_mode", text="Paint", icon="TPAINT_HLT", emboss=True).mode = "PAINT"

        if space.mode == "UV":
            row.operator("image_editor_extras.change_mode", text="UV", icon="UV", emboss=False).mode = "UV"
        else:
            row.operator("image_editor_extras.change_mode", text="UV", icon="UV", emboss=True).mode = "UV"

        if space.mode == "MASK":
            row.operator("image_editor_extras.change_mode", text="Mask", icon="MOD_MASK", emboss=False).mode = "MASK"
        else:
            row.operator("image_editor_extras.change_mode", text="Mask", icon="MOD_MASK", emboss=True).mode = "MASK"





    if space.show_region_tool_header:
        layout.prop(space, "show_region_tool_header", text="", icon="TRIA_UP")
    else:
        layout.prop(space, "show_region_tool_header", text="", icon="DOWNARROW_HLT")



def register():

    bpy.types.IMAGE_HT_header.append(draw_tool_settings_toogle)
    bpy.types.IMAGE_HT_tool_header.append(draw_image_editor_header)


def unregister():

    bpy.types.IMAGE_HT_header.remove(draw_tool_settings_toogle)
    bpy.types.IMAGE_HT_tool_header.remove(draw_image_editor_header)


if __name__ == "__main__":
    register()
