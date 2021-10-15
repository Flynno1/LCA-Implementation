import org.junit.Assert;
import org.junit.Test;

import static org.junit.Assert.*;

public class BSTTest {

    @Test
    public void testConstructor(){
        new BST();
    }

    @Test
    public void testEmpty(){

        BST bst = new BST();

        bst.LCA(2, 3);

    }

    @Test
    public void testInsert(){

        BST bst = new BST();
        bst.insert(1);
        bst.insert(10);
        bst.insert(4);
        bst.insert(8);
        bst.insert(13);
        bst.insert(2);


    }

    @Test
    public void testLCA(){

        BST bst = new BST();
        bst.insert(10);
        bst.insert(4);
        bst.insert(8);
        bst.insert(13);
        bst.insert(2);
        bst.insert(11);


        //        10
        //       /   \
        //     4       13
        //    / \     /
        //   2   8   11
        //


        Assert.assertEquals(bst.LCA(2, 11), 10);
        Assert.assertEquals(bst.LCA(4, 13), 10);
        Assert.assertEquals(bst.LCA(2, 8), 4);
        Assert.assertEquals(bst.LCA(2, 4), 4);




    }


}