class BST {

    class Node
    {
        int key;
        Node left, right;

        public Node(int item)
        {
            key = item;
            left = right = null;
        }
    }
    Node root;

    BST()
    {
        root = null;
    }

    // This method mainly calls insertRec()
    void insert(int key)
    {
        root = insertRec(root, key);
    }

    /* A recursive function to
    insert a new key in BST */
    Node insertRec(Node root, int key)
    {

		/* If the tree is empty,
		return a new node */
        if (root == null)
        {
            root = new Node(key);
            return root;
        }

        /* Otherwise, recur down the tree */
        if (key < root.key)
            root.left = insertRec(root.left, key);
        else if (key > root.key)
            root.right = insertRec(root.right, key);

        /* return the (unchanged) node pointer */
        return root;
    }

    public int LCA(int a, int b){

        return(lca(root, a, b));

    }

    int lca(Node lca, int a, int b){

        if (lca == null)
            return -1;

        // If both n1 and n2 are smaller than root, then LCA lies in left
        if (lca.key > a && lca.key > b) {
            return lca(lca.left, a, b);
        }

        // If both n1 and n2 are greater than root, then LCA lies in right
        if (lca.key < a && lca.key < b) {
            return lca(lca.right, a, b);
        }

        return lca.key;

    }


    // Driver Code
    public static void main(String[] args)
    {

    }
}