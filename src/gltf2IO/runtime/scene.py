import uuid
from src.gltf2IO.mixins.loggermixin import LoggerMixin

class Scene(LoggerMixin, object):
    def __init__(self):
        self._id = uuid.uuid1() 
        self.logger.debug('Initializing runtime scene')
        self._nodes = []

    @property
    def nodes(self):
        """Contains the runtime nodes within the scene
        
        Returns:
            [Node] -- [runtime Node]
        """

        return self._nodes

    @nodes.setter
    def nodes(self, value):
        """Set the nodes for the scene
        
        Arguments:
            value {list} -- [list of nodes in the scene]
        """
        self._nodes = value
