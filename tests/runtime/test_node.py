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

    if __name__ == '__main__':
        unittest.main()