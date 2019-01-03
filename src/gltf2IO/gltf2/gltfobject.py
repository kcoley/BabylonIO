from src.gltf2IO.mixins.loggermixin import LoggerMixin

class GLTFObject(LoggerMixin, object):
    def __init__(self):
        self.logger.debug('Creating glTF object')

        self._scenes = []

    @property
    def scenes(self):
        return self._scenes

    def write(self, file_location, export_options = None):
        """Write to disk
        
        Arguments:
            file_location {[type]} -- [description]
            export_options
        """


