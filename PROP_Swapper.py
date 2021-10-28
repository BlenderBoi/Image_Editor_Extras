import bpy


def ENUM_Swapper_A_Slot(self, context):
    items = [("NONE", "None","NONE")]

    Image = context.scene.swapper_a
    if Image:

        if Image.type == "RENDER_RESULT":
            items = []
            for index, slot in enumerate(Image.render_slots):
                item = (str(index), slot.name, slot.name)
                items.append(item)

    return items

def ENUM_Swapper_B_Slot(self, context):
    items = [("NONE", "None","NONE")]

    Image = context.scene.swapper_b
    if Image:

        if Image.type == "RENDER_RESULT":
            items = []
            for index, slot in enumerate(Image.render_slots):
                item = (str(index), slot.name, slot.name)
                items.append(item)

    return items
#
# def ENUM_Swapper_A_Layer(self, context):
#     item = [("NONE", "None","NONE")]
#
#
#
#     return items
#
# def ENUM_Swapper_B_Layer(self, context):
#     item = [("NONE", "None","NONE")]
#
#
#
#     return items
#
# def ENUM_Swapper_A_Pass(self, context):
#     item = [("NONE", "None","NONE")]
#
#
#
#     return item
#
# def ENUM_Swapper_B_Pass(self, context):
#     item = [("NONE", "None","NONE")]
#
#
#
#     return item


def register():

    bpy.types.Scene.swapper_a = bpy.props.PointerProperty(type=bpy.types.Image)
    bpy.types.Scene.swapper_b = bpy.props.PointerProperty(type=bpy.types.Image)

    bpy.types.Scene.swapper_a_slot = bpy.props.EnumProperty(items=ENUM_Swapper_A_Slot)
    bpy.types.Scene.swapper_b_slot = bpy.props.EnumProperty(items=ENUM_Swapper_B_Slot)

    # bpy.types.Scene.swapper_a_layer = bpy.props.EnumProperty(items=ENUM_Swapper_A_Layer)
    # bpy.types.Scene.swapper_b_layer = bpy.props.EnumProperty(items=ENUM_Swapper_B_Layer)
    #
    # bpy.types.Scene.swapper_a_pass = bpy.props.EnumProperty(items=ENUM_Swapper_A_Pass)
    # bpy.types.Scene.swapper_b_pass = bpy.props.EnumProperty(items=ENUM_Swapper_B_Pass)


def unregister():

    del bpy.types.Scene.swapper_a
    del bpy.types.Scene.swapper_b

    del bpy.types.Scene.swapper_a_slot
    del bpy.types.Scene.swapper_b_slot

    # del bpy.types.Scene.swapper_a_layer
    # del bpy.types.Scene.swapper_b_layer
    #
    # del bpy.types.Scene.swapper_a_pass
    # del bpy.types.Scene.swapper_b_pass


if __name__ == "__main__":
    register()
