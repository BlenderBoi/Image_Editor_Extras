import bpy


class IEH_OT_Swap_Image(bpy.types.Operator):
    """Swap Image"""
    bl_idname = "image_editor_extras.swap_image"
    bl_label = "Swap Image"
    bl_options = {'REGISTER', 'UNDO'}

    def draw(self, context):
        # layout = self.layout
        # scn = context.scene
        # Image = context.space_data.image
        # layout.prop(scn, "swapper_a", text="Image A")
        # layout.prop(scn, "swapper_b", text="Image B")

        layout = self.layout
        scene = context.scene
        Image = context.space_data.image

        Swapper_A = scene.swapper_a
        Swapper_B = scene.swapper_b
        # layout.operator("image_editor_extras.swap_image", text="Swap Image", icon="UV_SYNC_SELECT")
        layout.prop(scene, "swapper_a", text="Image A")
        if Swapper_A:
            if Swapper_A.type == "RENDER_RESULT":
                layout.prop(scene, "swapper_a_slot", text="Slot")

        layout.prop(scene, "swapper_b", text="Image B")

        if Swapper_B:
            if Swapper_B.type == "RENDER_RESULT":
                layout.prop(scene, "swapper_b_slot", text="Slot")









    def invoke(self, context, event):
        Image = context.space_data.image
        scn = context.scene
        A = scn.swapper_a
        B = scn.swapper_b

        if A and B:
            return self.execute(context)
        else:
            return context.window_manager.invoke_props_dialog(self)


    def execute(self, context):
        Image = context.space_data.image
        scn = context.scene
        A = scn.swapper_a
        B = scn.swapper_b



        #Redo and Fix Render Slot Problem

        if A and B:


            if A == B:

                context.space_data.image = A

                if A.type == "RENDER_RESULT":

                    if context.space_data.image.render_slot_changer == int(scn.swapper_a_slot)+1:

                        context.space_data.image.render_slot_changer = int(scn.swapper_b_slot)+1

                    elif context.space_data.image.render_slot_changer == int(scn.swapper_b_slot)+1:

                        context.space_data.image.render_slot_changer = int(scn.swapper_a_slot)+1

                    else:

                        context.space_data.image.render_slot_changer = int(scn.swapper_a_slot)+1
            else:


                if Image == A:
                    context.space_data.image = B

                    if B.type == "RENDER_RESULT":
                        context.space_data.image.render_slot_changer = int(scn.swapper_b_slot)+1


                elif Image == B:

                    context.space_data.image = A

                    if A.type == "RENDER_RESULT":
                        context.space_data.image.render_slot_changer = int(scn.swapper_a_slot)+1

                else:
                    context.space_data.image = A

                    if A.type == "RENDER_RESULT":
                        context.space_data.image.render_slot_changer = int(scn.swapper_a_slot)+1


        return {'FINISHED'}

classes = [IEH_OT_Swap_Image]

def register():

    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():

    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
