from src.gltf2IO.mixins.loggermixin import LoggerMixin

class Node(LoggerMixin, object):
    def __init__(self, name = None):
        """Initializes the node
        
        Arguments:
            LoggerMixin {LoggerMixin} -- [Logger for the node]
        
        Keyword Arguments:
            name {str} -- [Name of the node] (default: {None})
        """

        self.logger.debug('Initializing glTF node')
        self._name = name
        self._children = []
        self._translation = [0,0,0]
        self._rotation = [0,0,0,1]
        self._scale = [1,1,1]
        self._transform = None
        self._mesh = None

    @property
    def name(self):
        """Gets the name of the node
        
        Returns:
            [str] -- [The name of the node]
        """

        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of the node
        
        Arguments:
            name {str} -- [Sets the name of the node]
        """

        self._name = name

    @property
    def children(self):
        """Gets the children of the node
        
        Returns:
            [list] -- [list of children nodes]
        """

        return self._children

    @property
    def translation(self):
        """Gets the translation of the node
        """
        return self._translation

    @translation.setter
    def translation(self, value):
        """Sets the translation of the node
        
        Arguments:
            value {list} -- [list of floats representing translation]
        """

        self._translation = value


    @property
    def rotation(self):
        """Gets the quaternion rotation of the node
        """
        return self._rotation

    @rotation.setter
    def rotation(self, value):
        """Sets the rotation of the node
        
        Arguments:
            value {list} -- [list of floats representing quaternion [x,y,z,w]]
        """

        self._rotation = value

    @property
    def scale(self):
        """Gets the scale of the node
        """
        return self._scale

    @scale.setter
    def scale(self, value):
        """Sets the scale of the node

        Arguments:
            value {list} -- [list of floats representing scale]
        """
        self._scale = value

    @property
    def mesh(self):
        """Gets the mesh from the node
        """
        return self._mesh

    @mesh.setter
    def mesh(self, value):
        """Sets the mesh for the node
        
        Arguments:
            value {Mesh} -- [Mesh to add to node]
        """
        self._mesh = value




