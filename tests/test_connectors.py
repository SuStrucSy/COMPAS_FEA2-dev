import unittest
from compas_fea2.model.connectors import SpringConnector, ZeroLengthSpringConnector
from compas_fea2.model import Node
from compas_fea2.model import Part
from compas_fea2.model import SpringSection


class TestSpringConnector(unittest.TestCase):
    def test_initialization(self):
        node1 = Node([0, 0, 0])
        prt_1 = Part()
        prt_1.add_node(node1)
        node2 = Node([1, 0, 0])
        prt_2 = Part()
        prt_2.add_node(node2)
        section = SpringSection(axial=1, lateral=1, rotational=1)  # Replace with actual section class
        connector = SpringConnector(nodes=[node1, node2], section=section)
        self.assertEqual(connector.nodes, [node1, node2])


class TestZeroLengthSpringConnector(unittest.TestCase):
    def test_initialization(self):
        node1 = Node([0, 0, 0])
        prt_1 = Part()
        prt_1.add_node(node1)
        node2 = Node([1, 0, 0])
        prt_2 = Part()
        prt_2.add_node(node2)
        direction = [1, 0, 0]
        section = SpringSection(axial=1, lateral=1, rotational=1)
        connector = ZeroLengthSpringConnector(nodes=[node1, node2], direction=direction, section=section)
        self.assertEqual(connector.nodes, [node1, node2])
        self.assertEqual(connector.direction, direction)


if __name__ == "__main__":
    unittest.main()
