class Asset(object):
    def __init__(self, version = "2.0", generator=None):
        self._generator = generator
        self._version = version
        self._extensions = []
        self._extras = []

    @property
    def generator(self):
        '''Tool that generated this glTF model.  Useful for debugging
        
        Returns:
            [str] -- [The glTf generator string]
        '''

        return self._generator

    @generator.setter
    def generator(self, generator):
        """Sets the name of the generator for the asset
        
        Arguments:
            generator {str} -- [Name of the generator of the glTF asset]
        """

        self._generator = generator


    @property
    def version(self):
        '''The glTF version that this asset targets
        
        Returns:
            [str] -- [The glTF version number of this asset as a string]
        '''

        return self._version

    @version.setter
    def version(self, value):
        """Sets the glTf version number of the asset
        
        Arguments:
            value {str} -- [glTF version number as a string]
        """
        self._version = value


    @property
    def extensions(self):
        '''Extensions used for asset
        
        Returns:
            [dict] -- [dictionary of extensions]
        '''

        return self._extensions

    @property
    def extras(self):
        return self._extras

    def serialize(self):
        '''Serialize the asset to json
        
        Returns:
            [dict] -- [serialized json for asset]
        '''

        to_json = {
            'version': self._version
        }
        if self._generator:
            to_json['generator'] = self._generator
        return to_json