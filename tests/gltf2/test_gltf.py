import unittest
from src.babylonIO.gltf2 import GLTF, Node, Scene

class TestGLTF(unittest.TestCase):
    def setUp(self):
        self.generator_name = 'unit test'
        self.gltf = GLTF(self.generator_name)

    def test_serialize_empty(self):
        self.assertEqual(self.gltf.serialize(), 
        {
            'asset': 
            {
                'version': '2.0', 
                'generator': self.generator_name
            }
        }
        )

    def test_serialize_with_node(self):
        scene = Scene()
        node = Node('test node')
        scene.nodes = [node]
        self.gltf.create_scene([node])
        self.assertEqual(self.gltf.serialize(), 
        {
            'asset': 
            {
                'version': '2.0', 
                'generator': self.generator_name
            }, 
            'scenes': 
            [
                {
                    'nodes': 
                    [
                        0
                    ]
                }
            ], 
            'nodes': 
            [
                {
                    'name': 'test node'
                }
            ]
        }
        )
    
    def test_serialize_with_node_trs(self):
        scene = Scene()
        node = Node('test node')
        node.translation = [0,0,1]
        node.rotation = [0.707, 0, 0, 0.707]
        node.scale = [0.2, 1, 1]
        scene.nodes = [node]
        self.gltf.create_scene([node])
        self.assertEqual(self.gltf.serialize(), 
        {
            'asset': 
            {
                'version': '2.0', 
                'generator': self.generator_name
            }, 
            'scenes': 
            [
                {
                    'nodes': 
                    [
                        0
                    ]
                }
            ], 
            'nodes': 
            [
                {
                    'name': 'test node',
                    'translation': node.translation,
                    'rotation': node.rotation,
                    'scale' : node.scale
                }
            ]
        }
        )
    
    def test_serialize_with_two_nodes(self):
        scene = Scene()
        node = Node('test node')
        node2 = Node('test node2')
        nodes = [node, node2]
        scene.nodes = nodes
        self.gltf.create_scene(nodes)
        self.assertEqual(self.gltf.serialize(), 
        {
            'asset': 
            {
                'version': '2.0', 
                'generator': self.generator_name
            }, 
            'scenes': 
            [
                {
                    'nodes': 
                    [
                        0,
                        1
                    ]
                }
            ], 
            'nodes': 
            [
                {
                    'name': 'test node'
                },
                {
                    'name': 'test node2'
                }
            ]
        }
        )

    def test_serialize_with_two_nodes_trs(self):
        scene = Scene()
        node = Node('test node')
        node2 = Node('test node2')
        node2.translation = [0.2, 0, 0]
        nodes = [node, node2]
        scene.nodes = nodes
        self.gltf.create_scene(nodes)
        self.assertEqual(self.gltf.serialize(), 
        {
            'asset': 
            {
                'version': '2.0', 
                'generator': self.generator_name
            }, 
            'scenes': 
            [
                {
                    'nodes': 
                    [
                        0,
                        1
                    ]
                }
            ], 
            'nodes': 
            [
                {
                    'name': 'test node'
                },
                {
                    'name': 'test node2',
                    'translation': node2.translation
                }
            ]
        }
        )


        

if __name__ == '__main__':
    unittest.main()