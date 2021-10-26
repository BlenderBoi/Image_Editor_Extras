import bpy
import os
import pathlib



class RENDERUTILITY_PT_Render_Settings_Panel(bpy.types.Panel):
    """Render Settings Panel"""
    bl_label = "Render Settings Panel"
    bl_idname = "RENDERUTILITY_Render_Settings"
    bl_space_type = "IMAGE_EDITOR"
    bl_region_type = "WINDOW"

    def draw(self, context):

        layout = self.layout
        scene = context.scene
        rd = context.scene.render

        if rd.has_multiple_engines:
            layout.prop(rd, "engine", text="Render Engine")

        if rd.engine == 'CYCLES':
            cscene = scene.cycles
            col = layout.column()
            col.prop(cscene, "feature_set")

            col = layout.column()

            col.prop(cscene, "device")



        image_settings = rd.image_settings
        layout.template_image_settings(image_settings, color_management=False)



class RENDERUTILITY_OT_Pack_Render(bpy.types.Operator):
    """Pack Rendered Image"""
    bl_idname = "render_utility.pack_render"
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

        render_output = context.scene.render.filepath
        temp_directory = "/tmp/"
        name = "TEMP_PACK_BLENDER_RENDER_RESULT"

        filepath = os.path.join(temp_directory, name)
        # bpy.context.space_data.image.save_render(filepath, scene=bpy.context.scene)
        bpy.ops.image.save_as(save_as_render=True, copy=True, filepath=filepath, relative_path=True, show_multiview=False, use_multiview=False)


        # bpy.ops.render.render(write_still=True)



        if self.overwrite:
            check = bpy.data.images.get(self.image_name)
            if check:
                bpy.data.images.remove(check)

        Imported_Image = bpy.data.images.load(filepath)
        Imported_Image.pack()
        bpy.context.space_data.image = Imported_Image

        Imported_Image.name = self.image_name
        Imported_Image.use_fake_user = True
        Imported_Image.filepath = render_output + self.image_name

        return {'FINISHED'}


classes = [RENDERUTILITY_PT_Render_Settings_Panel, RENDERUTILITY_OT_Pack_Render]

def register():

    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():

    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
