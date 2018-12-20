import unittest
from graph import *

class TestList(unittest.TestCase):

    def test_01(self):
        g = Graph('test1.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.is_bipartite())

    def test_02(self):
        g = Graph('test2.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']])
        self.assertFalse(g.is_bipartite())
        self.assertEqual(g.get_vertex('v1'), g.vertex_list['v1'])

    def test_03(self):
        g = Graph("test3.txt")
        self.assertEqual(g.get_vertices(), ['v1', 'v10', 'v11', 'v12', 'v13', 'v14', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9'])
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9'], ['v10', 'v11'], ['v12', 'v13', 'v14']])
        self.assertTrue(g.is_bipartite())
        self.assertIsNone(g.get_vertex('v16'))

    def test_04(self):
        g = Graph("test4.txt")
        self.assertEqual(g.get_vertices(), ['v1', 'v2', 'v3'])
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3']])
        self.assertFalse(g.is_bipartite())

    def test_05(self):
        g = Graph("test5.txt")
        self.assertEqual(g.get_vertices(), ['v1', 'v2', 'v3', 'v4'])
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4']])
        self.assertFalse(g.is_bipartite())

    def test_06(self):
        g = Graph("test6.txt")
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v10', 'v11', 'v12', 'v13']])
        self.assertFalse(g.is_bipartite())

    def test_07(self):
        g = Graph("test7.txt")
        self.assertFalse(g.is_bipartite())

    def test_08(self):
        g = Graph("test8.txt")
        self.assertFalse(g.is_bipartite())

    def test_09(self):
        g = Graph("test9.txt")
        self.assertFalse(g.is_bipartite())

    def test_10(self):
        g = Graph("test10.txt")
        self.assertTrue(g.is_bipartite())

    def test_11(self):
        g = Graph("test11.txt")
        self.assertFalse(g.is_bipartite())

    # def test_12(self):
    #     g = Graph("test12.txt")
    #     self.assertFalse(g.is_bipartite())

    # def test_13(self):
    #     g = Graph("test13.txt")
    #     self.assertFalse(g.is_bipartite())

    # def test_14(self):
    #     g = Graph("test14.txt")
    #     self.assertFalse(g.is_bipartite())

if __name__ == '__main__':
   unittest.main()
