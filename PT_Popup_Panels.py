import bpy

class IEH_PT_Render_Settings_Panel(bpy.types.Panel):
    """Render Settings Panel"""
    bl_label = "Render Settings Panel"
    bl_idname = "IEH_PT_Render_Settings"
    bl_space_type = "IMAGE_EDITOR"
    bl_region_type = "WINDOW"

    def draw(self, context):

        layout = self.layout
        scene = context.scene
        rd = context.scene.render

        layout.label(text="Scene Camera")

        col = layout.column(align=True)

        col.prop(context.scene, "camera", text="", icon="CAMERA_DATA")
        col.prop(context.scene.render, "film_transparent", text="Transparent")
        col.separator()

        col.prop(context.scene, "frame_current", text="Frame")

        col.separator()
        layout.label(text="Resolution")
        row = col.row(align=True)
        row.prop(rd, "resolution_x", text="X")
        row.prop(rd, "resolution_y", text="Y")
        col.prop(rd, "resolution_percentage", text="%")

        layout.label(text="Render Settings")
        if rd.has_multiple_engines:
            layout.prop(rd, "engine", text="Engine")
            layout.separator()



        if rd.engine == 'CYCLES':
            cscene = scene.cycles
            col = layout.column()
            col.prop(cscene, "feature_set")

            col = layout.column()

            col.prop(cscene, "device")

        image_settings = rd.image_settings
        layout.template_image_settings(image_settings, color_management=False)

classes = [IEH_PT_Render_Settings_Panel]

def register():

    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():

    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()