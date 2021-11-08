class DAG {

    Node root;

    class Node
    {
        int key;
        List<Node> predicates;
        List<Node> succesors;

        public Node(int item)
        {
            key = item;
            connections = null;
            succesors = null;
        }


    }

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

    public int LCA(Node a, Node b){

        return(lca(root, a, b));

    }

    int lca(Node lca, Node a, Node b){

        if (lca == null)
            return -1;

        // If both a or b is the root retunr the root
        if (lca.key == a.key || lca.key == b.key) {
            return lca.key;
        }

        // if the two nodes aere the same return that node
        if (a.key == b.key) {
            return a;
        }

        List<Node> ca = new ArrayList<Node>();


        for(int i = 0; i<a.predicates.size(); i++){

            for(int j = 0; j<b.predicates.size(); j++){

                if(a.predicates[i].key == b.predicates[j].key){
                    ca.add(a.predicates[i].key);
                }

            }
        }

        if(ca.isEmpty()){
            return -1;
        }

        int max = ca.get(0);

        for (int i = 0; i<ca.size(); i++){

            if(max<ca.get(i)){
                max = ca.get(i);
            }

        }

        return max;

    }


    // Driver Code
    public static void main(String[] args)
    {

    }
}