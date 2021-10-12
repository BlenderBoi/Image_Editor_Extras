
bl_info = {
    "name": "Render Slot Slider",
    "author": "BlenderBoi",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "description": "Adds a Slider to Change Render Slots",
    "warning": "",
    "doc_url": "",
    "category": "Image Editor",
}

import bpy
from . import RenderSlotSlider

modules = [RenderSlotSlider]

def register():
    for module in modules:

        module.register()

def unregister():
    for module in modules:
        module.unregister()

if __name__ == "__main__":
    register()
