from src.babylonIO.mixins.loggermixin import LoggerMixin
from src.babylonIO.runtime import Scene, Node

class RuntimeIO(LoggerMixin, object):
    def __init__(self, is_right_handed = True):
        self._is_right_handed = is_right_handed
        self._scenes = []
        self._nodes = []

    @property
    def scenes(self):
        """Returns the scenes from runtime io
        
        Returns:
            [list] -- [list of scenes]
        """

        return self._scenes


    @classmethod
    def from_gltf(cls, gltf):
        """[Initialize the runtime from a glTF instance]
        
        Arguments:
            gltf {GLTF} -- [glTF instance]
        """
        runtimeio = RuntimeIO(is_right_handed=True)

        for gltf_scene in gltf.scenes:
            runtime_scene = Scene()
            runtime_nodes = [runtimeio._convert_gltf_node_to_runtime_node(gltf_node) for gltf_node in gltf_scene.nodes]
            if len(runtime_nodes) > 0:
                [runtimeio._nodes.append(runtime_node) for runtime_node in runtime_nodes if runtime_node not in runtimeio._nodes]
                runtime_scene.nodes = runtime_nodes
                runtimeio._scenes.append(runtime_scene)

        return runtimeio

    def _convert_gltf_node_to_runtime_node(self, gltf_node):
        runtime_node = Node(name=gltf_node.name)
        child_nodes = [self._convert_gltf_node_to_runtime_node(child_node) for child_node in gltf_node.children]
        if len(child_nodes) > 0:
            runtime_node.children = child_nodes

        return runtime_node



            

