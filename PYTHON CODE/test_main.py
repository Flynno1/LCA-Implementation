from unittest import TestCase


class Test(TestCase):
    def test_lca(self):
        root = self.Node(10)
        self.insert(root, 4);
        self.insert(root, 8);
        self.insert(root, 13);
        self.insert(root, 2);
        self.insert(root, 11);


        self.assertEqual(self.lca(root, 2, 11), 10)
        self.assertEqual(self.lca(root, 4, 13), 10)
        self.assertEqual(self.lca(root, 2, 8), 4)
        self.assertEqual(self.lca(root, 2, 4), 4)
