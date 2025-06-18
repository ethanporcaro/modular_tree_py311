import bpy
from ..base_types.node import MtreePropertyNode
from ...lib.m_tree import SimpleCurveProperty, PropertyWrapper

class RampPropertyNode(bpy.types.Node, MtreePropertyNode):
    bl_idname = "mt_RampPropertyNode"
    bl_label = "Ramp"

    property_type = SimpleCurveProperty

    def init(self, context):
        self.add_input("mt_PropertySocket", "start", property_name="y_min", property_value=.01)
        self.add_input("mt_PropertySocket", "end", property_name="y_max", property_value=1)
        self.add_input("mt_PropertySocket", "power", property_name="power", property_value=1)
        self.add_output("mt_PropertySocket", "value", is_property=False)
        