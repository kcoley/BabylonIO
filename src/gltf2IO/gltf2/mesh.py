from src.babylonIO.mixins.loggermixin import LoggerMixin

class Mesh(LoggerMixin, object):
    def __init__(self, name = None):
        """Initializes a mesh
        
        Arguments:
            LoggerMixin {[type]} -- [description]
        
        Keyword Arguments:
            name {str} -- [Name of the mesh] (default: {None})
        """
        self._name = name
        self._primitives = []

    @property
    def name(self):
        """Get the name of the mesh
        
        Returns:
            [str] -- [Name of the mesh]
        """

        return self._name

    @name.setter
    def name(self, value):
        """Set the name of the mesh
        
        Arguments:
            value {str} -- [Name to use for the mesh]
        """

        self._name = value

    @property
    def primitives(self):
        """Gets the list of mesh primitives from the mesh
        
        Returns:
            [list] -- [List of mesh primitives]
        """

        return self._primitives

    @primitives.setter
    def primitives(self, values):
        """Sets the mesh primitives of the mesh
        
        Arguments:
            values {list} -- [List of mesh primitives]
        """
        self._primitives = values


