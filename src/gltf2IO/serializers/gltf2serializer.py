from src.babylonIO.mixins.loggermixin import LoggerMixin

from src.babylonIO.gltf2.gltfobject import GLTFObject
from src.babylonIO.gltf2.scene import Scene as GLTFScene
from src.babylonIO.gltf2.node import Node as GLTFNode

class GLTF2Serializer(LoggerMixin, object):
    @staticmethod
    def serialize(self, runtime_instance, file_location):
        self.logger.debug('Serializing runtime instance to glTF 2.0')
        gltf_object = GLTFObject()
        for scene in runtime_instance.scenes:
            gltf_object.scenes.append(self._convert_scene_to_gltf(scene))

        gltf_object.write(file_location)

    @staticmethod
    def _convert_scene_to_gltf(self, runtime_scene):
        """Converts the runtime sceen to a glTF scene
        
        Arguments:
            runtime_scene {runtime scene} -- [runtime scene instance]
        """
        gltf_scene = GLTFScene()
        for child_node in runtime_scene.children:
            gltf_scene.nodes.append(self._convert_runtime_node_to_gltf(child_node))

    @staticmethod
    def _convert_runtime_node_to_gltf(self, runtime_node):
        gltf_node = GLTFNode(name = runtime_node.name)
        for runtime_child in runtime_node.children:
            gltf_node.children.append(self._convert_runtime_node_to_gltf(runtime_child))

        return gltf_node
        
