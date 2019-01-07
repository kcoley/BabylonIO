class Asset(object):
    def __init__(self, generator, version = "2.0"):
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

    @property
    def version(self):
        '''The glTF version that this asset targets
        
        Returns:
            [str] -- [The glTF version of this asset]
        '''

        return self._version

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
            'generator': self._generator,
            'version': self._version
        }
        return to_json