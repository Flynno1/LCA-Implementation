# Python program to demonstrate
# insert operation in binary search tree

# A utility class that represents
# an individual node in a BST


class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

# A utility function to insert
# a new node with the given key


def insert(root, key):
	if root is None:
		return Node(key)
	else:
		if root.val == key:
			return root
		elif root.val < key:
			root.right = insert(root.right, key)
		else:
			root.left = insert(root.left, key)
	return root


def lca(root, a, b):
	# Base Case
	if root is None:
		return -1

	# If both n1 and n2 are smaller than root, then LCA
	# lies in left
	if (root.data > a and root.data > b):
		return lca(root.left, a, b)

	# If both n1 and n2 are greater than root, then LCA
	# lies in right
	if (root.data < a and root.data < b):
		return lca(root.right, a, b)

	return root.val


