import bpy
import os
import pathlib
import tempfile

class IEH_OT_Duplicate_Pack(bpy.types.Operator):
    """Duplicate Pack"""
    bl_idname = "image_editor_extras.duplicate_pack"
    bl_label = "Duplicate (Pack)"
    bl_options = {'REGISTER', 'UNDO'}

    # name: bpy.props.StringProperty(name="Name")
    #
    # def invoke(self, context, event):
    #     Image = context.space_data.image
    #     self.name = Image.name
    #
    #     return context.window_manager.invoke_props_dialog(self)


    def execute(self, context):

        view_transform = context.scene.view_settings.view_transform

        render_output = context.scene.render.filepath
        temp_directory = tempfile.gettempdir()
        name = "TEMP_PACK_BLENDER_DUPLICATE_IMAGE"

        Image = context.space_data.image

        filepath = os.path.join(temp_directory, name)
        # bpy.context.space_data.image.save_render(filepath, scene=bpy.context.scene)

        try:

            Image = context.space_data.image

            if Image.type == "IMAGE":
                context.scene.view_settings.view_transform = "Standard"


            bpy.ops.image.save_as(save_as_render=True, copy=True, filepath=filepath, relative_path=True, show_multiview=False, use_multiview=False)

            # bpy.ops.render.render(write_still=True)


            Imported_Image = bpy.data.images.load(filepath)
            Imported_Image.pack()

            # Imported_Image.name = self.name
            NAME = Image.name
            Image.name = "TEMP"
            Imported_Image.name = NAME
            Image.name = NAME
            Imported_Image.use_fake_user = True
            Imported_Image.filepath = os.path.join(os.path.dirname(Image.filepath), Imported_Image.name)
            context.space_data.image = Imported_Image



        except:
            self.report({"INFO"}, message="Failed to Pack, Possibly an Empty Render Slot")


        context.scene.view_settings.view_transform = view_transform

        return {'FINISHED'}


classes = [IEH_OT_Duplicate_Pack]

def register():

    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():

    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
