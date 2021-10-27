import bpy
import os
import pathlib
import tempfile

class IEH_OT_Open_Viewport(bpy.types.Operator):
    """Open Viewport"""
    bl_idname = "image_editor_helper.open_viewport"
    bl_label = "Open Viewport"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.render.view_show("INVOKE_DEFAULT")



        # render = context.scene.render
        # res_x = render.resolution_x
        # res_y = render.resolution_y
        # res_p = render.resolution_percentage
        #
        # render.resolution_x = context.area.width
        # render.resolution_y = context.area.height
        # render.resolution_percentage = 100
        #
        # bpy.ops.render.view_show("INVOKE_DEFAULT")

        bpy.ops.screen.area_dupli("INVOKE_DEFAULT")
        area = bpy.context.window_manager.windows[-1].screen.areas[0]
        area.type = "VIEW_3D"

        # render.resolution_x = res_x
        # render.resolution_y = res_y
        # render.resolution_percentage = res_p


        for space in area.spaces:
            if space.type == "VIEW_3D":

                space.lock_camera = True
                space.region_3d.view_perspective = 'CAMERA'


        return {'FINISHED'}


classes = [IEH_OT_Open_Viewport]

def register():

    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():

    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
