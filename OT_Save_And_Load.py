import bpy
import os
import pathlib

#Render And Save
#Render at Next Slot
#Use Image Name If it is an Image

class IEH_OT_Save_And_Load(bpy.types.Operator):
    """Save and Load"""
    bl_idname = "image_editor_helper.save_and_load"
    bl_label = "Save and Load"
    bl_options = {'REGISTER', 'UNDO'}

    filepath: bpy.props.StringProperty(subtype="FILE_PATH")
    overwrite: bpy.props.BoolProperty(default=True)

    def draw(self, context):
        rd = context.scene.render
        image_settings = rd.image_settings
        layout = self.layout
        layout.label(text="This is Your Render Settings", icon="INFO")
        layout.template_image_settings(image_settings, color_management=False)
        layout.prop(self, "overwrite", text="Overwrite Existing Image Data")

    def invoke(self, context, event):

        scn = context.scene

        if self.filepath == "":
            self.filepath = context.scene.render.filepath
        else:
            if os.path.isdir(self.filepath):
                self.filepath = context.scene.render.filepath
            if os.path.isfile(self.filepath):
                self.filepath = pathlib.Path(context.scene.render.filepath).stem

        blend_file = pathlib.Path(bpy.data.filepath).stem
        if not blend_file == "":
            blend_file = blend_file + "_"

        name = blend_file + scn.name

        Image = context.space_data.image
        if Image.type == "IMAGE":
            name = Image.name


        self.filepath = os.path.join(self.filepath, name)



        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    def execute(self, context):

        view_transform = context.scene.view_settings.view_transform

        filepath = self.filepath

        format_check = pathlib.Path(self.filepath).suffix
        format = context.scene.render.file_extension



        if not format_check == format:
            self.filepath = self.filepath + format

            filepath = self.filepath


        try:
            Image = context.space_data.image

            if Image.type == "IMAGE":
                context.scene.view_settings.view_transform = "Standard"

            bpy.ops.image.save_as(save_as_render=True, copy=True, filepath=filepath, relative_path=True, show_multiview=False, use_multiview=False)


            if self.overwrite:
                image_name = pathlib.Path(filepath).name

                check = bpy.data.images.get(image_name)
                if check:
                    bpy.data.images.remove(check)


            Imported_Image = bpy.data.images.load(filepath)

            bpy.context.space_data.image = Imported_Image


        except:
            self.report({"INFO"}, message="Failed to Save, Possibly an Empty Render Slot")

        context.scene.view_settings.view_transform = view_transform

        return {'FINISHED'}


classes = [IEH_OT_Save_And_Load]

def register():

    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():

    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
