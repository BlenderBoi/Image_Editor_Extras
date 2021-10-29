import bpy

ENUM_Image_Editor_Mode = [("VIEW","View","View"),("PAINT","Paint","Paint"), ("MASK","Mask","Mask"), ("UV","UV","UV")]

class IEH_OT_Image_Editor_Mode(bpy.types.Operator):
    """Change Image Editor Mode"""
    bl_idname = "image_editor_extras.change_mode"
    bl_label = "Image Editor Mode"
    bl_options = {'REGISTER', 'UNDO'}


    mode: bpy.props.EnumProperty(items=ENUM_Image_Editor_Mode)

    def execute(self, context):
        area = context.area
        space = context.space_data
        if self.mode in ["VIEW", "PAINT", "MASK"]:
            space.ui_mode = self.mode

        if self.mode in ["UV"]:
            area.ui_type = "UV"
        # space.mode == self.mode

        return {'FINISHED'}


classes = [IEH_OT_Image_Editor_Mode]

def register():

    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():

    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
