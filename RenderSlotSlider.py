import bpy



def UPDATE_Slot_Changer(self, context):
    
    Image = context.space_data.image

    
    if Image:
        if Image.render_slot_changer > len(Image.render_slots):
            Image.render_slot_changer = len(Image.render_slots)
        else:
            Image.render_slots.active_index = Image.render_slot_changer - 1
        

def draw_item(self, context):
    
    layout = self.layout
    Image = context.space_data.image
    
    if Image:
        if Image.type == "RENDER_RESULT":
            layout.prop(Image, "render_slot_changer", text="Slot")


def register():

    bpy.types.Image.render_slot_changer = bpy.props.IntProperty(min=1, default=1, update=UPDATE_Slot_Changer)
    bpy.types.IMAGE_HT_header.append(draw_item)


def unregister():
    del bpy.types.Image.render_slot_changer
    bpy.types.IMAGE_HT_header.remove(draw_item)


if __name__ == "__main__":
    register()

