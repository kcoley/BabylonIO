import unittest

from src.gltf2IO.gltf2 import Node, Mesh
class TestNode(unittest.TestCase):
    def setUp(self):
        self.name = 'test'
        self.node = Node(self.name)
        self.child_node = Node('child node')
        self.node.children.append(self.child_node)

    def test_get_name(self):
        self.assertEqual(self.node.name, self.name)

    def test_set_name(self):
        new_name = 'new name'
        self.node.name = new_name
        self.assertEqual(self.node.name, new_name)

    def test_children(self):
        self.assertTrue(self.node.children[0], self.child_node)

    def test_get_translation(self):
        self.assertEqual(self.node.translation, [0,0,0])

    def test_set_translation(self):
        translation = [1,0,0]
        self.node.translation = translation
        self.assertEqual(self.node.translation, translation)

    def test_get_rotation(self):
        self.assertEqual(self.node.rotation, [0,0,0,1])

    def test_set_rotation(self):
        rotation = [0,0,0,1]
        self.node.rotation = rotation
        self.assertEqual(self.node.rotation, rotation)

    def test_get_scale(self):
        self.assertEqual(self.node.scale, [1,1,1])

    def test_set_scale(self):
        scale = [0.5, 1,1]
        self.node.scale = scale
        self.assertEqual(self.node.scale, scale)

    def test_get_mesh(self):
        self.assertEqual(self.node.mesh, None)

    def test_set_mesh(self):
        mesh = Mesh()
        self.node.mesh = mesh
        self.assertEqual(self.node.mesh, mesh)

    


if __name__ == '__main__':
    unittest.main()