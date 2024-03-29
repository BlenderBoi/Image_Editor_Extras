import bpy
import os
import pathlib
import tempfile

class IEH_OT_Pack_Render(bpy.types.Operator):
    """Pack Rendered Image"""
    bl_idname = "image_editor_extras.pack_render"
    bl_label = "Pack Render"
    bl_options = {'REGISTER', 'UNDO'}

    image_name: bpy.props.StringProperty(default="Image00")
    overwrite: bpy.props.BoolProperty(default=True)





    def draw(self, context):
        layout = self.layout

        layout.prop(self, "image_name", text="Image")
        layout.prop(self, "overwrite", text="Overwrite")

    def invoke(self, context, event):

        blend_file = pathlib.Path(bpy.data.filepath).stem

        scn = context.scene

        if not blend_file == "":
            blend_file = blend_file + "_"

        self.image_name = blend_file + scn.name

        return context.window_manager.invoke_props_dialog(self)



    def execute(self, context):

        # view_transform = context.scene.view_settings.view_transform
        # context.scene.view_settings.view_transform = "Standard"

        render_output = context.scene.render.filepath
        temp_directory = tempfile.gettempdir()
        name = "TEMP_PACK_BLENDER_RENDER_RESULT"

        filepath = os.path.join(temp_directory, name)

        # bpy.context.space_data.image.save_render(filepath, scene=bpy.context.scene)

        try:
            bpy.ops.image.save_as(save_as_render=True, copy=True, filepath=filepath, relative_path=True, show_multiview=False, use_multiview=False)

            # bpy.ops.render.render(write_still=True)
            check = None

            if self.overwrite:
                check = bpy.data.images.get(self.image_name)
                if check:
                    check.name = "TEMP_PACK_BLENDER_RENDER_RESULT_OVERWRITE"


            Imported_Image = bpy.data.images.load(filepath)
            Imported_Image.pack()
            bpy.context.space_data.image = Imported_Image



            Imported_Image.name = self.image_name
            Imported_Image.use_fake_user = True

            if self.overwrite:
                if check:
                    if Imported_Image:

                        check.user_remap(Imported_Image)
                        bpy.data.images.remove(check)
                    else:
                        check.name = self.image_name


            relative_directory = "//Textures/"

            rel_path = relative_directory + self.image_name
            tmp_path = temp_directory + self.image_name

            blend_file = pathlib.Path(bpy.data.filepath).stem

            if blend_file:
                for packed_file in Imported_Image.packed_files:
                    packed_file.filepath = rel_path




        except:
            self.report({"INFO"}, message="Failed to Pack, Possibly an Empty Render Slot")

        # context.scene.view_settings.view_transform = view_transform

        return {'FINISHED'}


classes = [IEH_OT_Pack_Render]

def register():

    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():

    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
