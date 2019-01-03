import uuid

from src.gltf2IO.mixins.loggermixin import LoggerMixin

class Node(LoggerMixin, object):
    """Represents a runtime node
    """

    def __init__(self, name = None):
        """Creates a runtime node
        
        Keyword Arguments:
            name {str} -- [runtime node name] (default: {None})
        """

        self._id = uuid.uuid1()
        self._name = name
        self._children = []
        self.logger.debug("Created runtime Node instance {}".format(self._id))
      
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
            name {str} -- [The name of the node]
        """

        self._name = name

    @property
    def children(self):
        """Contains the children nodes of this node
        
        Returns:
            [[Node]] -- [Children nodes]
        """

        return self._children




            
