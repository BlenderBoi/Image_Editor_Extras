import bpy
import os
import pathlib
import tempfile

class IEH_OT_Open_Viewport(bpy.types.Operator):
    """Open Viewport"""
    bl_idname = "image_editor_helper.open_viewport"
    bl_label = "Toogle Viewport"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # bpy.ops.render.view_show("INVOKE_DEFAULT")


        # bpy.ops.screen.area_join(cursor=(0, 0))

        # bpy.ops.screen.area_dupli("INVOKE_DEFAULT")

        View_3D_Check = False

        for area in context.screen.areas:
            if area.type == "VIEW_3D":
                View_3D_Check = True

                Area_1 = None
                Area_2 = area


                for area2 in context.screen.areas:
                    if area2.type == "IMAGE_EDITOR":
                        Area_1 = area2

                if Area_1 and Area_2:
                    bpy.ops.screen.area_swap(cursor=(Area_1.width, Area_1.y))
                    # bpy.ops.screen.area_join("INVOKE_DEFAULT", cursor=(Area_1.width, Area_1.y))

                    bpy.ops.screen.area_join(cursor=(Area_1.width, Area_1.y))
                    bpy.ops.screen.new()


                    break
                    # return {'FINISHED'}
                    # bpy.ops.render.view_show("INVOKE_DEFAULT")


                break

        if View_3D_Check:
            pass

        else:
            start_area = context.area
            start_areas = context.screen.areas[:]

            bpy.ops.screen.area_split(direction='VERTICAL', factor=0.7)
            areas = context.window_manager.windows[-1].screen.areas

            for area in areas:
                if area not in start_areas:
                    area.type = "VIEW_3D"

                    for space in area.spaces:
                        if space.type == "VIEW_3D":
                            space.show_region_header = False
                            space.lock_camera = True
                            space.region_3d.view_perspective = 'CAMERA'
                            space.overlay.show_overlays = False
                            space.show_gizmo = False

        context.view_layer.update()


        for screen in bpy.data.screens:
            for area in screen.areas:
                area.tag_redraw()

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