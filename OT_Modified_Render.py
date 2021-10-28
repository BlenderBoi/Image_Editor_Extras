import bpy


class IEH_OT_Modified_Render(bpy.types.Operator):
    """Render"""
    bl_idname = "image_editor_helper.render"
    bl_label = "Render"
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):


        for image in bpy.data.images:
            if image.type == "RENDER_RESULT":
                context.space_data.image = image

        bpy.ops.render.render("EXEC_DEFAULT")
        return {'FINISHED'}

classes = [IEH_OT_Modified_Render]

def register():

    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():

    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
