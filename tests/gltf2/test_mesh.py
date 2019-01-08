import unittest

from src.babylonIO.gltf2 import Mesh
class TestMesh(unittest.TestCase):
    def setUp(self):
        self.mesh_name = 'some_mesh'
        self.mesh = Mesh(name=self.mesh_name)

    def test_get_name(self):
        self.assertEqual(self.mesh.name, self.mesh_name)

    def test_set_name(self):
        name = 'new name'
        self.mesh.name = name
        self.assertEqual(self.mesh.name, name)

