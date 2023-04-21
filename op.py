import bpy


class LIGHTHELPER_OT_AddLight(bpy.types.Operator):
    """
    Add light to a scene using a dialog
    """

    bl_idname = "object.lighthelper_add_light"
    bl_label = "Add Light Dialog"
    bl_description = "Add light dialog menu"
    bl_options = {"REGISTER", "UNDO"}

    prop_light_enum: bpy.props.EnumProperty(
        name="light type",
        description="light type enum",
        items=[
            ("POINT", "Point", "Point"),
            ("SUN", "Sun", "Sun"),
            ("SPOT", "Spot", "Spot"),
            ("AREA", "Area", "Area"),
        ],
        default="POINT",
    )

    def execute(self, context):
        bpy.ops.object.light_add(type=self.prop_light_enum)
        return {"FINISHED"}

    def invoke(self, context, event):
        """
        display dialog to select the light type
        """
        scene = context.scene
        wm = context.window_manager

        self.prop_light_enum = scene.LIGHTHELPER_prop_light_enum
        return wm.invoke_props_dialog(self)


class LIGHTHELPER_OT_DeleteLight(bpy.types.Operator):
    """
    Delete light
    """

    bl_idname = "object.lighthelper_delete_light"
    bl_label = "Delete target light"
    bl_description = "Delete target Light"
    bl_options = {"REGISTER", "UNDO"}

    object_name: bpy.props.StringProperty()

    def execute(self, context):
        # delete target object
        bpy.ops.object.select_all(action="DESELECT")
        bpy.data.objects[self.object_name].select_set(state=True)
        bpy.ops.object.delete()

        return {"FINISHED"}


def init_props():
    scene = bpy.types.Scene
    # Light enum
    scene.LIGHTHELPER_prop_light_enum = bpy.props.EnumProperty(
        name="light type",
        description="light type enum",
        items=[
            ("POINT", "Point", "Point"),
            ("SUN", "Sun", "Sun"),
            ("SPOT", "Spot", "Spot"),
            ("AREA", "Area", "Area"),
        ],
        default="POINT",
    )


def clear_props():
    scene = bpy.types.Scene
    del scene.LIGHTHELPER_prop_light_enum
