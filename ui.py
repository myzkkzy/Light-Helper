import bpy
from .op import LIGHTHELPER_OT_AddLight, LIGHTHELPER_OT_DeleteLight


class LIGHTHELPER_PT_LightPanel(bpy.types.Panel):
    """
    Creates a Panel in the Object properties window
    """

    bl_label = "Light Helper"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "LightHelper"
    bl_context = "objectmode"

    def draw(self, context):
        layout = self.layout

        # button
        btn_row = layout.row(align=True)
        btn_row.alignment = "LEFT"
        btn_row.operator(
            LIGHTHELPER_OT_AddLight.bl_idname, text="ADD LIGHT", icon="ADD"
        )
        layout.separator()

        # header
        # NOTE: Using draw_header() interferes with the panel. Use row() instead.
        header_row = layout.row(align=True)
        header_row.label(text="Name")
        header_row.label(text="Color")
        header_row.label(text="Energy")
        header_row.label(text="Type")
        layout.separator()

        # Display a list of all lights in the scene
        for light in context.scene.objects:
            if light.type == "LIGHT":
                row = layout.row(align=True)
                row.label(text=light.name)  # NOTE: Name should be changed from Outliner
                row.prop(light.data, "color")
                row.prop(light.data, "energy")
                row.prop(light.data, "type")
                row.operator(
                    LIGHTHELPER_OT_DeleteLight.bl_idname, text="DELETE", icon="REMOVE"
                ).object_name = light.name

    @classmethod
    def poll(cls, context):
        return True  # always display
