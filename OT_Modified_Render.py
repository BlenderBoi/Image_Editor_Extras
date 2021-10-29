import bpy


class IEH_OT_Modified_Render(bpy.types.Operator):
    """Render"""
    bl_idname = "image_editor_extras.render"
    bl_label = "Render"
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):


        for image in bpy.data.images:
            if image.type == "RENDER_RESULT":
                context.space_data.image = image

        # bpy.ops.render.render("EXEC_DEFAULT")
        render_display_type = context.preferences.view.render_display_type

        context.preferences.view.render_display_type = "NONE"

        bpy.ops.render.render("INVOKE_DEFAULT",use_viewport=True)

        context.preferences.view.render_display_type = render_display_type


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
