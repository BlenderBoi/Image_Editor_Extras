import bpy

ENUM_Direction = [("NEXT","Next","Next"),("BACK","Back","Back")]


class RENDER_SLOT_SLIDER_MT_Swapper_Menu(bpy.types.Menu):
    bl_label = "Render Slot Swapper Menu"
    bl_idname = "RENDER_SLOT_SWAPPER_MT_menu"

    def draw(self, context):

        layout = self.layout
        Image = context.space_data.image
        if not Image.set_active_as_swapper_a:
            layout.prop(Image, "swapper_a", text="Slot A")
        layout.prop(Image, "swapper_b", text="Slot B")
        layout.prop(Image, "set_active_as_swapper_a", text="Use Active as A")


class RENDER_SLOT_SLIDER_OT_Next_Slot(bpy.types.Operator):
    """Next / Previous Slot"""
    bl_idname = "render_slot_slider.operator"
    bl_label = "Render Slot"
    bl_options = {'REGISTER', 'UNDO'}

    direction: bpy.props.EnumProperty(items=ENUM_Direction)

    # @classmethod
    # def poll(cls, context):
    #
    #     if context.space_data == "IMAGE_EDITOR":
    #         return True

    def execute(self, context):
        Image = context.space_data.image
        if self.direction == "NEXT":
            if Image:
                Image.render_slot_changer += 1
        if self.direction == "BACK":
            if Image:
                Image.render_slot_changer -= 1

        return {'FINISHED'}



class RENDER_SLOT_SLIDER_OT_Swapper(bpy.types.Operator):
    """Slot Swapper"""
    bl_idname = "render_slot_slider.swapper"
    bl_label = "Swapper"
    bl_options = {'REGISTER', 'UNDO'}



    def execute(self, context):
        Image = context.space_data.image
        Swapper_A = Image.swapper_a
        Swapper_B = Image.swapper_b

        if Image.render_slot_changer == Image.swapper_a:
            Image.render_slot_changer = Image.swapper_b
        else:
            if Image.render_slot_changer == Image.swapper_b:
                Image.render_slot_changer = Image.swapper_a
            else:
                if Image.set_active_as_swapper_a:
                    if not Image.swapper_a == Image.swapper_b:
                        Image.swapper_a = Image.render_slot_changer
                        Image.render_slot_changer = Image.swapper_b
                    else:
                        Image.render_slot_changer = Image.swapper_a
                else:
                    Image.render_slot_changer == Image.swapper_a


        return {'FINISHED'}

def UPDATE_Slot_Changer(self, context):

    Image = context.space_data.image


    if Image:
        if Image.render_slot_changer > len(Image.render_slots):
            Image.render_slot_changer = len(Image.render_slots)
        else:
            Image.render_slots.active_index = Image.render_slot_changer - 1


def UPDATE_Swapper_Max(self, context):

    Image = context.space_data.image
    if Image:
        if Image.swapper_a > len(Image.render_slots):
            Image.swapper_a = len(Image.render_slots)
        if Image.swapper_b > len(Image.render_slots):
            Image.swapper_b = len(Image.render_slots)


def draw_item_pre(self, context):
    layout = self.layout
    Image = context.space_data.image

    if Image:
        if Image.type == "RENDER_RESULT":

            row = layout.row(align=True)
            operator = row.operator("render.render", icon="RENDER_STILL")
            operator.use_viewport=False


def draw_item(self, context):

    layout = self.layout
    Image = context.space_data.image

    if Image:
        if Image.type == "RENDER_RESULT":

            row = layout.row(align=True)
            operator = row.operator("render_slot_slider.operator", text="", icon="TRIA_LEFT")
            operator.direction = "BACK"
            row.prop(Image, "render_slot_changer", text="Slot")
            operator = row.operator("render_slot_slider.operator", text="", icon="TRIA_RIGHT")
            operator.direction = "NEXT"


            row = layout.row(align=True)


            operator = row.operator("render.render", icon="RESTRICT_RENDER_OFF")
            row.popover("RENDERUTILITY_Render_Settings", text='', text_ctxt='', translate=True, icon='NONE', icon_value=0)

            row.operator("render_utility.pack_render", text="Pack", icon="PACKAGE")
            row.operator("image.save_as", text="Save", icon="FILE_TICK")


            # row = layout.row(align=True)
            # operator = row.operator("render_slot_slider.swapper", text="", icon="UV_SYNC_SELECT")
            # row.menu("RENDER_SLOT_SWAPPER_MT_menu", text="", icon="TOOL_SETTINGS")
            #



        if not Image.type == "RENDER_RESULT":
            row = layout.row(align=True)
            if not Image.packed_file:
                row.operator("image.pack", text="Pack", icon="PACKAGE")
            else:
                row.label(text="Packed", icon="PACKAGE")
                operator = row.operator("file.unpack_item", icon="REMOVE")
                operator.id_type = 19785
                operator.id_name = Image.name
                # row.operator("image.unpack", text="Unpack", icon="TRASH")

            row.operator("image.save", text="Save", icon="FILE_TICK")
            row.separator()
            operator = row.operator("render_utility.remove_image", text="", icon="TRASH")
            operator.image_name = Image.name

classes = [RENDER_SLOT_SLIDER_MT_Swapper_Menu, RENDER_SLOT_SLIDER_OT_Swapper, RENDER_SLOT_SLIDER_OT_Next_Slot]


def register():

    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Image.render_slot_changer = bpy.props.IntProperty(min=1, default=1, update=UPDATE_Slot_Changer)

    bpy.types.Image.swapper_a = bpy.props.IntProperty(min=1, default=1, update=UPDATE_Swapper_Max)
    bpy.types.Image.swapper_b = bpy.props.IntProperty(min=1, default=2, update=UPDATE_Swapper_Max)

    bpy.types.Image.set_active_as_swapper_a = bpy.props.BoolProperty(default=True)

    bpy.types.IMAGE_HT_header.append(draw_item)


def unregister():

    for cls in classes:
        bpy.utils.unregister_class(cls)

    del bpy.types.Image.render_slot_changer

    bpy.types.IMAGE_HT_header.remove(draw_item)

    del bpy.types.Image.swapper_a
    del bpy.types.Image.swapper_b
    del bpy.types.Image.set_active_as_swapper_a

if __name__ == "__main__":
    register()
