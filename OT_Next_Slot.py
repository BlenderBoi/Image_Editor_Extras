import bpy

ENUM_Direction = [("NEXT","Next","Next"),("BACK","Back","Back")]

class IEH_OT_Next_Slot(bpy.types.Operator):
    """Next / Previous Slot"""
    bl_idname = "image_editor_extras.next_slot"
    bl_label = "Render Slot"
    bl_options = {'REGISTER', 'UNDO'}

    direction: bpy.props.EnumProperty(items=ENUM_Direction)

    def execute(self, context):
        Image = context.space_data.image
        if self.direction == "NEXT":
            if Image:
                Image.render_slot_changer += 1
        if self.direction == "BACK":
            if Image:
                Image.render_slot_changer -= 1

        return {'FINISHED'}

classes = [IEH_OT_Next_Slot]

def register():

    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():

    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
