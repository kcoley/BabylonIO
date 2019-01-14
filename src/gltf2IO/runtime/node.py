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
        self._translation = [0,0,0]
        self._rotation = [0,0,0,1]
        self._scale = [1,1,1]
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




            
