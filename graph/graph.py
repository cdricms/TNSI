from turtle import width
from typing import Set, Type, Any, Dict
import json

from simplejson import JSONEncoder

class Encoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, (set, list)):
            return [i.node.value for i in o]

        return o.__dict__

        

class RepresentationMixin:

    def __str__(self):
        return self.toJSON()

    def toJSON(self):
        return json.dumps(self, cls=Encoder, check_circular=True, indent=2)

    __repr__ = __str__


class Node(RepresentationMixin):
    value: Any = None
    neighbours: Set[Type["Edge"]] 

    def __init__(self, value: Any):
        self.value = value
        self.neighbours = set()

    def add_neighbour(self, node: "Node", weight=0):
        edge = Edge(node, weight)
        self.neighbours.add(edge)

    def remove_neighbour(self, node: Type["Node"]):
        removed = False
        for edge in self.neighbours:
            if edge.node== node:
                self.neighbours.remove(edge)
                removed = True

        return removed

    @property
    def length(self):
        return len(self.neighbours)


class Edge:
    node = Any
    def __init__(self, node, weight=0):
        self.node = node
        self.weight = weight



class Graph(RepresentationMixin):
    nodes: Dict[Type[Node.value], Type[Node]] = {}


    def __init__(self):
        self.nodes = {}


    def add_node(self, node: Node):
        if not self.nodes.get(node.value):
            self.nodes[node.value] = node

        return self.nodes.get(node.value)


    def add_neighbour(self, node: Node, o: Node):
        if not self.get_node(node.value):
            self.add_node(node)

        if not self.get_node(o.value):
            self.add_node(o)
        
        node.add_neighbour(o)
        o.add_neighbour(node)


    def remove_neighbour(self, node: Node, o: Node):
        a = node.remove_neighbour(o)
        b = o.remove_neighbour(node)

        return a, b


    def get_node(self, value: Type[Node.value]):
        return self.nodes.get(value)


    @property
    def length(self):
        return len(self.nodes)


    def bsf(self):
        pass


def main():
    g = Graph()
    g.add_node(Node("hello"))

    print("First")
    print(g)

    g.add_neighbour(g.get_node("hello"), Node("world"))

    print("Second")
    print(g)

    g.add_neighbour(g.get_node("hello"), Node("foo"))
    print("Third")
    print(g)

    g.remove_neighbour(g.get_node("hello"), g.get_node("world"))

    print("Fourth")
    print(g)

if __name__ == "__main__":

    main()