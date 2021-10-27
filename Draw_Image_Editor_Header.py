import bpy

from . import Utility_Functions

def draw_image_editor_header(self, context):

    layout = self.layout
    Image = context.space_data.image
    preferences = Utility_Functions.get_addon_preferences()

    row = layout.row(align=True)

    if preferences.BTN_Open_Viewport:
        operator = row.operator("image_editor_helper.open_viewport", icon="VIEW3D")
        row.separator()

    if preferences.BTN_Render:
        operator = row.operator("render.render", icon="RESTRICT_RENDER_OFF")
    if preferences.PROP_Render_Percentage:
        row.prop(context.scene.render, "resolution_percentage", text="Size")
    if preferences.PROP_Frame:
        row.prop(context.scene, "frame_current", text="Frame")

    if preferences.POPUP_Render_Settings:
        row.popover("IEH_PT_Render_Settings", text='', text_ctxt='', translate=True, icon='NONE', icon_value=0)

    if Image:

        if Image.type == "RENDER_RESULT":

            if preferences.PROP_Slot_Changer:

                row = layout.row(align=True)
                operator = row.operator("image_editor_helper.next_slot", text="", icon="TRIA_LEFT")
                operator.direction = "BACK"
                row.prop(Image, "render_slot_changer", text="Slot")
                operator = row.operator("image_editor_helper.next_slot", text="", icon="TRIA_RIGHT")
                operator.direction = "NEXT"

            row = layout.row(align=True)

            # if preferences.BTN_Render:
            #     operator = row.operator("render.render", icon="RESTRICT_RENDER_OFF")
            # if preferences.POPUP_Render_Settings:
            #     row.popover("IEH_PT_Render_Settings", text='', text_ctxt='', translate=True, icon='NONE', icon_value=0)


            if preferences.POPUP_Render_Settings or preferences.BTN_Render:
                row = layout.row(align=True)

            if preferences.BTN_Pack:
                row.operator("image_editor_helper.pack_render", text="Pack", icon="PACKAGE")
            if preferences.BTN_Save:
                # row.operator("image.save_as", text="Save As", icon="FILE_TICK")
                row.operator("image_editor_helper.save_and_load", text="Save As and Load", icon="FILE_TICK")

        if not Image.type == "RENDER_RESULT":

            row = layout.row(align=True)
            if preferences.BTN_Pack:
                if not Image.packed_file:
                    if Image.type == "IMAGE":
                        row.operator("image.pack", text="Pack", icon="PACKAGE")

                else:
                    row.label(text="Packed", icon="PACKAGE")
                    operator = row.operator("file.unpack_item", icon="REMOVE")
                    operator.id_type = 19785
                    operator.id_name = Image.name

            if Image.type == "IMAGE":
                if preferences.BTN_Duplicate:
                    row.operator("image_editor_helper.duplicate_pack", text="Duplicate (Pack)", icon="DUPLICATE")
                    row.separator()

            if preferences.BTN_Save:
                if Image.is_dirty:
                    row.operator("image.save", text="Save*", icon="FILE_TICK")

                # row.operator("image.save_as", text="Save As", icon="FILE_TICK")
                row.operator("image_editor_helper.save_and_load", text="Save As and Load", icon="FILE_TICK")

            if preferences.BTN_Remove:
                row.separator()
                operator = row.operator("image_editor_helper.remove_image", text="", icon="TRASH")
                operator.image_name = Image.name



def register():

    bpy.types.IMAGE_HT_header.append(draw_image_editor_header)
    # bpy.types.IMAGE_HT_tool_header.append(draw_image_editor_header)


def unregister():

    bpy.types.IMAGE_HT_header.remove(draw_image_editor_header)
    # bpy.types.IMAGE_HT_tool_header.append(draw_image_editor_header)


if __name__ == "__main__":
    register()
