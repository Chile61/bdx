import os
import bpy
from .. import utils as ut


class ExternJava(bpy.types.Operator):
    """Make internal java files external"""
    bl_idname = "object.externjava"
    bl_label = "Make internal java files external"

    def execute(self, context):
        ut.save_internal_java_files(ut.src_root(), overwrite=True)

        # Delete internal java texts
        version = float("{}.{}".format(*bpy.app.version))
        for t in bpy.data.texts:
            if t.name.endswith(".java"):
                if version >= 2.78:
                    bpy.data.texts.remove(t, True)
                else:
                    bpy.data.texts.remove(t)

        # Refresh text editor(s) hack
        for area in bpy.context.screen.areas:
            for space in area.spaces:
                if space.type == "TEXT_EDITOR":
                    space.show_margin = not space.show_margin
                    space.show_margin = not space.show_margin

        return {'FINISHED'}


def register():
    bpy.utils.register_class(ExternJava)


def unregister():
    bpy.utils.unregister_class(ExternJava)
