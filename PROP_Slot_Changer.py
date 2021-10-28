import bpy

def UPDATE_Slot_Changer(self, context):

    Image = context.space_data.image

    if Image:
        if Image.render_slot_changer > len(Image.render_slots):
            Image.render_slot_changer = len(Image.render_slots)
        else:
            Image.render_slots.active_index = Image.render_slot_changer - 1




def register():

    bpy.types.Image.render_slot_changer = bpy.props.IntProperty(min=1, default=1, update=UPDATE_Slot_Changer)

def unregister():

    del bpy.types.Image.render_slot_changer


if __name__ == "__main__":
    register()
