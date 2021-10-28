
bl_info = {
    "name": "Image Editor Helper",
    "author": "BlenderBoi",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "description": "Some Helper in Image Editor",
    "warning": "",
    "doc_url": "",
    "category": "Image Editor",
}


import bpy

from . import Draw_Image_Editor_Header
from . import OT_Next_Slot
from . import OT_Pack_Render
from . import OT_Remove_Image
from . import Preferences
from . import PROP_Slot_Changer
from . import PT_Popup_Panels
from . import OT_Swap_Image

from . import OT_Duplicate_Pack

from . import OT_Save_And_Load

from . import OT_Open_Viewport
from . import OT_Modified_Render
from . import OT_Image_Editor_Mode

from . import PROP_Swapper

modules = [OT_Swap_Image, PROP_Swapper, OT_Image_Editor_Mode, OT_Modified_Render, OT_Open_Viewport, OT_Duplicate_Pack, OT_Save_And_Load, PT_Popup_Panels, Draw_Image_Editor_Header, OT_Next_Slot, OT_Pack_Render, OT_Remove_Image, PROP_Slot_Changer, Preferences]

def register():
    for module in modules:

        module.register()

def unregister():
    for module in modules:
        module.unregister()

if __name__ == "__main__":
    register()
