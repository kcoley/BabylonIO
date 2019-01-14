import unittest

from src.gltf2IO import runtime
from src.gltf2IO import gltf2

class TestRuntimeIO(unittest.TestCase):
    def test_from_gltf(self):
        gltf = gltf2.GLTF('unit test')
        gltf.create_scene([gltf2.Node('test node')])
        runtimeio = runtime.RuntimeIO.from_gltf(gltf)
        self.assertEqual(runtimeio.scenes[0].nodes[0].name, 'test node')
        

if __name__ == '__main__':
    unittest.main()

    

