import bpy

class RENDERUTILITY_OT_Remove_Image(bpy.types.Operator):
    """Remove Image"""
    bl_idname = "render_utility.remove_image"
    bl_label = "Remove Image"
    bl_options = {'REGISTER', 'UNDO'}

    image_name: bpy.props.StringProperty()


    def execute(self, context):

        image = bpy.data.images.get(self.image_name)
        if image:
            bpy.data.images.remove(image)

        return {'FINISHED'}


classes = [RENDERUTILITY_OT_Remove_Image]

def register():

    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():

    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
