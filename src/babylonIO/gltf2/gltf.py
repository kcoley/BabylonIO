from src.babylonIO.mixins.loggermixin import LoggerMixin

from scene import Scene
from asset import Asset

class GLTF(LoggerMixin, object):
    """Represents a glTF instance
    """

    def __init__(self, generator_name):
        self.logger.debug('Creating glTF object')
        self._asset = Asset(generator=generator_name)

        self._scenes = []
        self._nodes = []

    @property
    def scenes(self):
        """Returns a list of glTF scenes
        
        Returns:
            [list] -- [list of glTF scenes]
        """

        return self._scenes

    def create_scene(self, nodes):
        scene = Scene()
        scene.nodes = nodes
        self._scenes.append(scene)
        [self._add_node_to_nodes(node) for node in nodes]


    def _add_node_to_nodes(self, node):
        if node not in self._nodes:
            self._nodes.append(node)
        for child in node.children:
            self._add_node_to_nodes(child)



    def serialize(self, make_glb=False):
        """Serialize the glTF document
        
        Arguments:
            make_glb {bool} -- [Boolean specifiying if a glb should be generated]
        """
        document = {}
        document['asset'] = self._asset.serialize()
        nodes = [self._serialize_node(node) for node in self._nodes]
        if len(nodes) > 0:
            document['nodes'] = nodes

        scenes = [self._serialize_scene(scene) for scene in self._scenes]
        if len(scenes) > 0:
            document['scenes'] = scenes

        return document

    def _serialize_node(self, node):
        gltf_node = {}
        if node.name:
            gltf_node['name'] = node.name
        if node.translation != [0,0,0]:
            gltf_node['translation'] = node.translation
        if node.rotation != [0,0,0,1]:
            gltf_node['rotation'] = node.rotation
        if node.scale != [1,1,1]:
            gltf_node['scale'] = node.scale
        children = []
        for child in node.children:
            children.append(self._nodes.index(child))
        if len(children) > 0:
            gltf_node['children'] = children

        return gltf_node

    def _serialize_scene(self, scene):
        gltf_scene = {}
        gltf_nodes = []
        
        for node in scene.nodes:
            gltf_nodes.append(self._nodes.index(node))

        if len(gltf_nodes) > 0:
            gltf_scene['nodes'] = gltf_nodes

        return gltf_scene





