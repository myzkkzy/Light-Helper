bl_info = {
    "name": "Light Helper",
    "author": "k_miya",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Panel > Light Helper",
    "description": "operate lights in the scene.",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Lighting",
}

if "bpy" in locals():
    import importlib

    importlib.reload(ui)
    importlib.reload(op)
else:
    from .ui import LIGHTHELPER_PT_LightPanel
    from .op import LIGHTHELPER_OT_AddLight, LIGHTHELPER_OT_DeleteLight

import bpy

classes = [
    LIGHTHELPER_PT_LightPanel,
    LIGHTHELPER_OT_AddLight,
    LIGHTHELPER_OT_DeleteLight,
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    op.init_props()


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    op.clear_props()


if __name__ == "__main__":
    register()
