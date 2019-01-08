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