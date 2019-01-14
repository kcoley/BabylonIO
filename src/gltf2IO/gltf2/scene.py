from src.gltf2IO.mixins.loggermixin import LoggerMixin

class Scene(LoggerMixin, object):
    def __init__(self):
        """Initializes the glTF scene
        
        Arguments:
            LoggerMixin {LoggerMixin} -- [Logger for the scene]
        """

        self.logger.debug('Creating glTF scene')
        self._nodes = []


    @property
    def nodes(self):
        """Gets the nodes from the scene
        
        Returns:
            [list] -- [list of nodes int the scene]
        """

        return self._nodes

    @nodes.setter
    def nodes(self, value):
        """Sets the nodes for the scene
        
        Arguments:
            value {[list]} -- [list of nodes to set for the scene]
        """
        self._nodes = value

