import unittest

from src.babylonIO.gltf2 import Asset

class TestAsset(unittest.TestCase):
    def setUp(self):
        self.asset = Asset('unit test')

    def test_generator(self):
        self.assertEqual(self.asset.generator, 'unit test')

    def test_version(self):
        self.assertEqual(self.asset.version, '2.0')

    def test_serialize(self):
        to_json = self.asset.serialize()
        self.assertEqual(to_json, {'generator': 'unit test', 'version': '2.0'})


if __name__ == '__main__':
    unittest.main()