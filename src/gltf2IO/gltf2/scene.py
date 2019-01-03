from src.gltf2IO.mixins.loggermixin import LoggerMixin

class Scene(LoggerMixin, object):
    def __init__(self):
        self.logger.debug('Creating glTF scene')
        self._nodes = []


    @property
    def nodes(self):
        return self._nodes
