import bpy
import os

script_file = os.path.realpath(__file__)
addon_directory = os.path.dirname(script_file)
addon_name = os.path.basename(addon_directory)

def get_addon_preferences():
    addon_preferences = bpy.context.preferences.addons[addon_name].preferences
    return addon_preferences

def get_addon_name():
    return addon_name
