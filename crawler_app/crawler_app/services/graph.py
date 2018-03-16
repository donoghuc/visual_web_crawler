from crawler_app.services.helpers import get_domain

'''Holds nodes and edges lists of the crawled graph'''
class Graph:
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def add_node(self, node, node_id):
        node.id = node_id
        self.nodes.append(node)

    def add_edge(self, parent_id, target_id):
        edge = Edge(parent_id, target_id)
        self.edges.append(edge)

'''Holds data about the page node (page that is crawled)'''
class Page_Node:
    __slots__ =('url', 'parents_list', 'domain', 'parent_node', 'id', 'node_depth', 'keyword', 'found')
    def __init__(self, url, parents_list, node_depth, id = None, parent_node = None, keyword = None):
        self.url = url
        self.parents_list = parents_list
        self.domain = get_domain(self.url)
        self.node_depth = int(node_depth)
        self.id = id
        self.parent_node = parent_node
        self.keyword = keyword
        self.found = False

'''Edge between a parent and child page'''
class Edge:
    __slots__ = ['parent', 'target']
    def __init__(self, parent, target):
        self.parent = parent
        self.target = target
        