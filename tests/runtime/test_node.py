import unittest

from src.gltf2IO.runtime.node import Node

class TestNode(unittest.TestCase):
    def setUp(self):
        self.node = Node(name='Test')
        child_node = Node(name='Child Node')
        self.node.children.append(child_node)

    def test_get_name(self):
        self.assertEqual(self.node.name, 'Test')

    def test_set_name(self):
        name = 'Example'
        self.node.name = name
        self.assertEqual(self.node.name, name)

    def test_get_children(self):
        children = self.node.children
        self.assertEqual(len(children), 1)
        self.assertEqual(children[0].name, 'Child Node')

    def test_set_children(self):
        child = Node(name='Another Child Node')
        self.node.children.append(child)

        get_child = self.node.children[-1]
        self.assertEqual(child, get_child)

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

    if __name__ == '__main__':
        unittest.main()