from enum import Enum

class PrimitiveMode(Enum):
    """Primitive mode enum for mesh primitives
    """
    POINTS = 0
    LINES = 1
    LINE_LOOP = 2
    LINE_STRIP = 3
    TRIANGLES = 4
    TRIANGLE_STRIP = 5
    TRIANGLE_FAN = 6

class PrimitiveAttribute(Enum):
    """Primitive attribute enum for mesh primitives
    """
    POSITION = 'POSITION'
    NORMAL = 'NORMAL'
    TANGENT = 'TANGENT'
    TEXCOORD_0 = 'TEXCOORD_0'
    TEXCOORD_1 = 'TEXCOORD_1'
    COLOR_0 = 'COLOR_0'
    JOINTS_0 = 'JOINTS_0'
    WEIGHTS_0 = 'WEIGHTS_0'



class MeshPrimitive(object):
    """Geometry to be rendered with the given material
    """

    def __init__(self):
        self._attributes = {}
        self._indices = []
        self._material = None
        self._mode = PrimitiveMode.TRIANGLES
        self._targets = []

    @property
    def mode(self):
        """Get the primitive mode
        
        Returns:
            [PrimitiveMode] -- [The primitive mode]
        """

        return self._mode

    @mode.setter
    def mode(self, value):
        """Sets the primitive mode
        
        Arguments:
            value {PrimitiveMode} -- [Primitive mode to set]
        """

        self._mode = value

    @property
    def indices(self):
        """Gets the indices of the mesh primitive
        """
        return self._indices

    @indices.setter
    def indices(self, value):
        """Sets the indices for the mesh primitive
        
        Arguments:
            value {list} -- [list of indices]
        """
        self._indices = value

    def get_attribute(self, primitive_attribute):
        """Gets the primitive attribute based on type
        
        Arguments:
            primitive_attribute {PrimitiveAttribute} -- [The type of primitive attribute to get]
        
        Returns:
            [list] -- [list of attribute values]
        """

        return self._attributes[primitive_attribute] if primitive_attribute in self._attributes else []

    def set_attribute(self, primitive_attribute, value):
        """Sets the primitive attribute based on type
        
        Arguments:
            primitive_attribute {PrimitiveAttribute} -- [The type of primitive attribute to set]
            value {list} -- [values to set for the primitive attribute]
        """

        self._attributes[primitive_attribute] = value



