import bpy
import os
from . import Utility_Functions





class IEH_user_preferences(bpy.types.AddonPreferences):

    bl_idname = Utility_Functions.get_addon_name()

    BTN_Render: bpy.props.BoolProperty(default=True, name="Render Button")
    BTN_Pack: bpy.props.BoolProperty(default=True, name="Pack Button")
    BTN_Save: bpy.props.BoolProperty(default=True, name="Save Button")
    BTN_Remove: bpy.props.BoolProperty(default=True, name="Remove Image Button")
    BTN_Duplicate: bpy.props.BoolProperty(default=True, name="Duplicate Pack Button")
    BTN_Open_Viewport: bpy.props.BoolProperty(default=True, name="Toogle Viewport")
    BTN_Mode_Changer: bpy.props.BoolProperty(default=True, name="Mode Changer")

    POPUP_Render_Settings: bpy.props.BoolProperty(default=True, name="Render Settings Popup")
    PROP_Slot_Changer: bpy.props.BoolProperty(default=True, name="Slot Changer")
    PROP_Render_Percentage: bpy.props.BoolProperty(default=True, name="Render Percentage")
    PROP_Frame: bpy.props.BoolProperty(default=True, name="Frame")

    POPUP_Image_Swapper: bpy.props.BoolProperty(default=True, name="Image Swapper")

    def draw(self, context):
        layout = self.layout

        layout.prop(self, "BTN_Render")
        layout.prop(self, "BTN_Pack")
        layout.prop(self, "BTN_Save")
        layout.prop(self, "BTN_Remove")
        layout.prop(self, "BTN_Duplicate")
        layout.prop(self, "BTN_Open_Viewport")
        layout.prop(self, "BTN_Mode_Changer")
        layout.prop(self, "POPUP_Image_Swapper")


        layout.prop(self, "PROP_Slot_Changer")
        layout.prop(self, "PROP_Render_Percentage")
        layout.prop(self, "PROP_Frame")
        layout.prop(self, "POPUP_Render_Settings")

classes = [IEH_user_preferences]



def register():
    for cls in classes:

        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
