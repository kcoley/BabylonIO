from __future__ import absolute_import
import json

from src.gltf2IO.mixins.loggermixin import LoggerMixin

from .scene import Scene
from .asset import Asset
from .node import Node
from .mesh import Mesh
from .meshprimitive import MeshPrimitive

class GLTF(LoggerMixin, object):
    """Represents a glTF instance
    """

    def __init__(self, generator_name):
        self.logger.debug('Creating glTF object')
        self._asset = Asset(generator=generator_name)

        self._scenes = []
        self._nodes = []

    @classmethod
    def deserialize(cls, gltf_data):
        """Deserialize glTF json to glTF object
        
        Arguments:
            gltf_data {glTF json data} -- [json data for glTF]
        """
        gltf = GLTF(generator_name='gltf2IO')
        if 'asset' in gltf_data:
            asset = gltf_data['asset']
            gltf_asset = Asset(generator='gltf2IO')
            if 'version' in asset:
                gltf_asset.version = asset['version']
                
            if 'generator' in asset:
                gltf_asset.generator = asset['generator']
            gltf.asset = gltf_asset
        
        if 'nodes' in gltf_data:
            for node in gltf_data['nodes']:
                gltf_node = Node(node['name'] if 'name' in node else None)
                if 'transform' in node:
                    gltf_node.transform = node['transform']
                else:
                    if 'translation' in node:
                        gltf_node.translation = node['translation']
                    if 'rotation' in node:
                        gltf_node.rotation = node['rotation']
                    if 'scale' in node:
                        gltf_node.scale = node['scale']
                gltf.nodes.append(gltf_node)
            for node_index, node in enumerate(gltf_data['nodes']):
                if 'children' in node:
                    for child_node_index in node['children']:
                        gltf.nodes[node_index].children.append(gltf.nodes[child_node_index])



        if 'scenes' in gltf_data:
            for scene in gltf_data['scenes']:
                gltf_scene = Scene()
                nodes = []
                if 'nodes' in scene:
                    for node_index in scene['nodes']:
                        nodes.append(gltf.nodes[node_index])
                    gltf.create_scene(nodes)

        if 'meshes' in gltf_data:
            for mesh in gltf_data['meshes']:
                gltf_mesh = Mesh()
                if 'primitives' in mesh:
                    for primitive in mesh['primitives']:
                        gltf_primitive = MeshPrimitive()
                        if 'attributes' in primitive:
                            attributes = primitive['attributes']
                            if 'POSITION' in attributes:
                                print('POSITION')
                            if 'NORMAL' in attributes:
                                print('NORMAL')
                            if 'TANGENT' in attributes:
                                print('TANGENT')
                            if 'COLOR_0' in attributes:
                                print('COLOR_0')
                            if 'TEXCOORD_0' in attributes:
                                print('TEXCOORD_0')
                            if 'TEXCOORD_1' in attributes:
                                print('TEXCOORD_1')
                            gltf_mesh.primitives.append(gltf_primitive)

        return gltf


        if 'nodes' in gltf_data:
            for node in gltf_data['nodes']:
                gltf_node = Node(name = node['name'] if 'name' in node else None)
                #TRS data
                if 'transform' in node:
                    gltf_node.transform = node['transform']
                else:
                    if 'translation' in node:
                        gltf_node.translation = node['translation']
                    if 'rotation' in node:
                        gltf_node.rotation = node['rotation']
                    if 'scale' in node:
                        gltf_node.scale = node['scale']

                #Mesh data
                #Skin data
                gltf.nodes.append(gltf_node)

            #now handle children
            for node_index, node in enumerate(gltf_data['nodes']):
                if 'children' in node:
                    for child_index in node['children']:
                        gltf.nodes[node_index].append(gltf.nodes[child_index])
    
        if 'scenes' in gltf_data:
            for scene in gltf_data['scenes']:
                gltf_scene = Scene()
                for node_index in scene:
                    gltf_scene.nodes.append(gltf.nodes[node_index])
                gltf.scenes.append(gltf_scene)
                    




            

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

    @property
    def asset(self):
        """Gets the glTF asset data
        """
        return self._asset

    @asset.setter
    def asset(self, value):
        """Sets the glTF asset data
        """
        self._asset = value

    @property
    def nodes(self):
        """Get the nodes in the glTF file:
        """
        return self._nodes

    @nodes.setter
    def nodes(self, value):
        """Sets the nodes in the glTF file
        
        Arguments:
            value {[Node]} -- [List of Nodes]
        """
        self._nodes = value


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





