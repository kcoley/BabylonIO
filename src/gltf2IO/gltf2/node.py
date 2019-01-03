from src.gltf2IO.mixins.loggermixin import LoggerMixin

class Node(LoggerMixin, object):
    def __init__(self, name = None):
        self.logger.debug('Initializing glTF node')
        self._name = name
        self._children = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def children(self):
        return self._children