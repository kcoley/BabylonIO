import unittest
from src.gltf2IO.gltf2 import GLTF, Node, Scene, Asset

class TestGLTF(unittest.TestCase):
    def setUp(self):
        self.generator_name = 'unit test'
        self.gltf = GLTF(generator_name=self.generator_name)

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

    def test_deserialize_empty(self):
        serialized = self.gltf.serialize()
        result = GLTF.deserialize(serialized)
        self.assertEqual(result.serialize(), serialized)

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

    def test_deserialize_with_node(self):
        scene = Scene()
        node = Node(name='test node')
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

        serialized = self.gltf.serialize()
        gltf = GLTF.deserialize(serialized)
        self.assertEqual(gltf.serialize(), serialized)

    
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

    def test_deserialize_with_node_trs(self):
        scene = Scene()
        node = Node('test node')
        node.translation = [0,0,1]
        node.rotation = [0.707, 0, 0, 0.707]
        node.scale = [0.2, 1, 1]
        scene.nodes = [node]
        self.gltf.create_scene([node])

        serialized = self.gltf.serialize()
        gltf = GLTF.deserialize(serialized)
        self.assertEqual(serialized, gltf.serialize())
    
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

    def test_deserialize_with_two_nodes(self):
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
        serialized = self.gltf.serialize()
        gltf = GLTF.deserialize(serialized)
        self.assertEqual(serialized, gltf.serialize())

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

    def test_deserialize_with_two_nodes_trs(self):
        scene = Scene()
        node = Node('test node')
        node2 = Node('test node2')
        node2.translation = [0.2, 0, 0]
        nodes = [node, node2]
        scene.nodes = nodes
        self.gltf.create_scene(nodes)

        serialized = self.gltf.serialize()
        gltf = GLTF.deserialize(serialized)
        self.assertEqual(serialized, gltf.serialize())

    def test_serialize_with_two_nodes_hierarchy_trs(self):
        node = Node('test node')
        node2 = Node('test node2')
        node2.translation = [0.2, 0, 0]
        node.children.append(node2)
        nodes = [node]
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
                        0
                    ]
                }
            ], 
            'nodes': 
            [
                {
                    'name': 'test node',
                    'children': [1]
                },
                {
                    'name': 'test node2',
                    'translation': node2.translation
                }
            ]
        }
        )

    def test_deserialize_with_two_nodes_hierarchy_trs(self):
        node = Node('test node')
        node2 = Node('test node2')
        node2.translation = [0.2, 0, 0]
        node.children.append(node2)
        nodes = [node]
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
                        0
                    ]
                }
            ], 
            'nodes': 
            [
                {
                    'name': 'test node',
                    'children': [1]
                },
                {
                    'name': 'test node2',
                    'translation': node2.translation
                }
            ]
        }
        )
        serialized = self.gltf.serialize()
        gltf = GLTF.deserialize(serialized)
        self.assertEqual(serialized, gltf.serialize())
        
    
    def test_get_asset(self):
        asset = self.gltf.asset
        self.assertEqual(asset.generator, self.generator_name)

    def test_set_asset(self):
        asset = Asset('test asset')
        self.gltf.asset = asset

        self.assertEqual(self.gltf.asset, asset)

    def test_get_nodes(self):
        nodes = self.gltf.nodes
        self.assertEqual(self.gltf.nodes, [])

    def test_set_nodes(self):
        nodes = []
        nodes.append(Node('nodeA'))
        self.gltf.nodes = nodes
        self.assertEqual(len(self.gltf.nodes), 1)
        self.assertEqual(self.gltf.nodes[0], nodes[0])

    def test_get_scenes(self):
        scenes = self.gltf.scenes
        self.assertEqual(scenes, [])

    def test_set_scenes(self):
        nodes = []
        nodes.append(Node('nodeA'))
        nodes.append(Node('nodeB'))
        self.gltf.create_scene(nodes) 
        self.assertEqual(self.gltf.scenes[0].nodes, nodes)




        

if __name__ == '__main__':
    unittest.main()