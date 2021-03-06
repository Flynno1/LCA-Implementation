from DAG import DAG
import unittest


class MyTestCase(unittest.TestCase):

    # test for add one node
    def test1_addNode(self):
        DAG1 = DAG()
        DAG1.addNode('a')
        DAG1.printDAG(DAG1.graph)
        self.assertTrue(DAG1.graph == {'a': []})

    # test for a non-existent node
    def test2_addNode(self):
        DAG2 = DAG()
        DAG2.addNode('b')
        self.assertFalse(DAG2.graph == {'a': []})

    # test for a non-existent node just after init
    def test3_addNode(self):
        DAG3 = DAG()
        self.assertFalse(DAG3.addNode('a'))

    # further testing addNode Function
    def test4_addNode(self):
        DAG4 = DAG()
        self.assertFalse(DAG4.addNode('a'))
        self.assertFalse(DAG4.addNode('b'))
        self.assertFalse(DAG4.addNode('c'))
        self.assertFalse(DAG4.addNode('d'))
        self.assertFalse(DAG4.addNode('e'))
        self.assertFalse(DAG4.addNode('f'))

    # test to see if there are cycles in graph
    def test1_DAG(self):
        DAG5 = DAG()
        DAG5.addNode('1')
        DAG5.addNode('2')
        DAG5.addEdge('3', '4')
        DAG5.addNode('5')
        DAG5.addNode('6')
        DAG5.addEdge('2', '3')
        DAG5.addEdge('3', '1')
        self.assertFalse(DAG5.DFS(DAG5.graph))
        self.assertTrue(DAG5)

    # test to see if there are cycles in graph
    def test2_DAG(self):
        DAG6 = DAG()
        DAG6.addNode('1')
        DAG6.addNode('2')
        DAG6.addEdge('1', '2')
        self.assertTrue(DAG6)
        self.assertTrue(DAG6.DFS(DAG6.graph))

    # test to see if there are cycles in graph
    def test3_DAG(self):
        DAG7 = DAG()
        DAG7.addNode('1')
        DAG7.addNode('2')
        DAG7.addNode('4')
        DAG7.addEdge('2', '4')
        self.assertTrue(DAG7)
        self.assertTrue(DAG7.DFS(DAG7.graph))

    # test for LCA of two nodes in a DAG where nodes are integers
    def test1_LCA(self):
        DAG8 = DAG()
        DAG8.addNode(1)
        DAG8.addNode(2)
        DAG8.addNode(3)
        DAG8.addNode(4)
        DAG8.addNode(5)
        DAG8.addNode(6)
        DAG8.addNode(7)
        DAG8.addNode(8)
        DAG8.addEdge(1, 2)
        DAG8.addEdge(1, 3)
        DAG8.addEdge(1, 6)
        DAG8.addEdge(2, 3)
        DAG8.addEdge(3, 5)
        DAG8.addEdge(2, 6)
        DAG8.addEdge(5, 6)
        DAG8.addEdge(6, 7)
        DAG8.addEdge(4, 7)
        DAG8.addEdge(8, 7)
        DAG8.LCA(DAG8.graph, 7, 3)
        self.assertTrue(DAG8.LCA(DAG8.graph, 7, 3) == 3)

    # test for LCA of two nodes in a DAG where nodes are strings
    def test2_LCA(self):
        DAG9 = DAG()
        DAG9.addNode('a')
        DAG9.addNode('b')
        DAG9.addNode('c')
        DAG9.addNode('d')
        DAG9.addNode('e')
        DAG9.addNode('f')
        DAG9.addNode('g')
        DAG9.addNode('h')
        DAG9.addEdge('a', 'b')
        DAG9.addEdge('a', 'c')
        DAG9.addEdge('a', 'd')
        DAG9.addEdge('b', 'c')
        DAG9.addEdge('c', 'e')
        DAG9.addEdge('b', 'f')
        DAG9.addEdge('e', 'f')
        DAG9.addEdge('f', 'h')
        DAG9.addEdge('d', 'g')
        DAG9.LCA(DAG9.graph, 'h', 'e')
        self.assertTrue(DAG9.LCA(DAG9.graph, 'h', 'e') == 'e')

    # test for LCA of two nodes in a DAG where nodes are strings
    def test3_LCA(self):
        DAG10 = DAG()
        DAG10.addNode('a')
        DAG10.addNode('b')
        DAG10.addNode('c')
        DAG10.addNode('d')
        DAG10.addNode('e')
        DAG10.addNode('f')
        DAG10.addNode('g')
        DAG10.addNode('h')
        DAG10.addEdge('a', 'b')
        DAG10.addEdge('a', 'c')
        DAG10.addEdge('a', 'd')
        DAG10.addEdge('b', 'c')
        DAG10.addEdge('b', 'f')
        DAG10.addEdge('c', 'e')
        DAG10.addEdge('d', 'g')
        DAG10.addEdge('e', 'f')
        DAG10.addEdge('f', 'h')
        self.assertTrue(DAG10.LCA(DAG10.graph, 'h', 'g') == 'a')
        self.assertTrue(DAG10.LCA(DAG10.graph, 'a', 'g') == 'a')
        self.assertFalse(DAG10.LCA(DAG10.graph, 'g', 'b') == 'b')
        self.assertFalse(DAG10.LCA(DAG10.graph, 'h', 'f') == 'b')

    # test for LCA of a node and a non-node in graph
    def test4_LCA(self):
        DAG11 = DAG()
        DAG11.addNode('x')
        DAG11.addNode('y')
        DAG11.addNode('z')
        DAG11.addEdge('x', 'y')
        self.assertTrue(DAG11.LCA(DAG11.graph, 'a', 'x') == None)

    # test for LCA of an empty graph
    def test5_LCA(self):
        DAG12 = DAG()
        self.assertTrue(DAG12.LCA(DAG12.graph, None, None) == None)


if __name__ == '__main__':
    unittest.main()
