from __future__ import absolute_import
import unittest

from src.babylonIO.gltf2.meshprimitive import MeshPrimitive, PrimitiveMode, PrimitiveAttribute

class TestMeshPrimitive(unittest.TestCase):
    def setUp(self):
        self.meshprimitive = MeshPrimitive()

    def test_get_mode(self):
        self.assertEqual(self.meshprimitive.mode, PrimitiveMode.TRIANGLES)

    def test_set_mode(self):
        self.meshprimitive.mode = PrimitiveMode.TRIANGLE_FAN
        self.assertEqual(self.meshprimitive.mode, PrimitiveMode.TRIANGLE_FAN)

    def test_get_indices(self):
        self.assertEqual(self.meshprimitive.indices, [])

    def test_set_indices(self):
        indices = [1,3,6]
        self.meshprimitive.indices = indices
        self.assertEqual(self.meshprimitive.indices, indices)

    def test_get_positions(self):
        self.assertEqual(self.meshprimitive.get_attribute(PrimitiveAttribute.POSITION), [])

    def test_set_positions(self):
        positions = [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (2.0, 0.0, 1.0)]
        self.meshprimitive.set_attribute(PrimitiveAttribute.POSITION, positions)
        self.assertEqual(self.meshprimitive.get_attribute(PrimitiveAttribute.POSITION), positions)

    def test_get_normals(self):
        self.assertEqual(self.meshprimitive.get_attribute(PrimitiveAttribute.NORMAL), [])

    def test_set_normals(self):
        normals = [(1.0, 0.0, 0.0), (1.0, 0.0, 0.0), (1.0, 0.0, 0.0)]
        self.meshprimitive.set_attribute(PrimitiveAttribute.NORMAL, normals)
        self.assertEqual(self.meshprimitive.get_attribute(PrimitiveAttribute.NORMAL), normals)
