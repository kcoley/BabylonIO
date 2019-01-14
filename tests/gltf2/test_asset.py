import unittest

from src.gltf2IO.gltf2 import Asset

class TestAsset(unittest.TestCase):
    def setUp(self):
        self.asset = Asset(generator='unit test')

    def test_generator(self):
        self.assertEqual(self.asset.generator, 'unit test')

    def test_get_version(self):
        self.assertEqual(self.asset.version, '2.0')

    def test_set_version(self):
        self.asset.version = '2.1'
        self.assertEqual(self.asset.version, '2.1')

    def test_serialize(self):
        to_json = self.asset.serialize()
        self.assertEqual(to_json, {'generator': 'unit test', 'version': '2.0'})


if __name__ == '__main__':
    unittest.main()