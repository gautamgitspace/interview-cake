package CTCI4_1;

/**
 * Created by Gautam on 8/16/16.
 */
public class TreeNode
{
    public   TreeNode left;
    public   TreeNode right;
    public   TreeNode parent;
    public   int data;
    public   int size;

    /*DEF CONS*/
    public TreeNode(int d)
    {
        data=d;
        size = 0;
    }
    /*SET LEFT CHILD*/
    public void setLeftChild(TreeNode left)
    {
        this.left=left;
        if(left!=null)
        {
            left.parent=this;
        }
    }
    /*SET RIGHT CHILD*/
    public void setRightChild(TreeNode right)
    {
        this.right=right;
        if(right!=null)
        {
            right.parent=this;
        }
    }
    /*INSERT ELEMENTS IN ORDER*/
    public   void insert(int d)
    {
        if(d<=data)
        {
            if(left==null)
            {
                setLeftChild(new TreeNode(d));
            }
            else
            {
                left.insert(d);
            }
        }
        else
        {
            if(right==null)
            {
                setRightChild(new TreeNode(d));
            }
            else
            {
                right.insert(d);
            }
        }
        size++;
    }

    /*HEIGHT OF TREE*/
    public int height()
    {
        int leftHeight = left!=null ? left.height() : 0;
        int rightHeight = right!=null ? right.height() : 0;
        return 1+ Math.max(leftHeight, rightHeight);
    }

    /*BINARY TREE VALIDATOR*/
    public boolean binaryTreeValidator()
    {
        if(left!=null)
        {
            if (data < left.data || left.binaryTreeValidator())
                return false;
        }
        if(right!=null)
        {
            if (data >= right.data || right.binaryTreeValidator())
                return false;
        }
        return true;
    }

    /*SEARCH BST*/
    public TreeNode search(int d)
    {
        if(d==data)
            return this;
        if(d<data)
        {
            return left!=null ? left.search(d) : null;
        }
        else if(d>data)
        {
            return right!=null ? right.search(d) : null;
        }
        return null;
    }
    /*RETURN SIZE*/
    public int getSize()
    {
        return size;
    }
    /*IN-ORDER TRAVERSAL*/
    public static void inOrderTraversal(TreeNode t)
    {
        if(t!=null)
        {
            if(t.left!=null)
            {
                inOrderTraversal(t.left);
            }
            System.out.println(t.data);
            if(t.right!=null)
            {
                inOrderTraversal(t.right);
            }
        }
    }
    /*PRE-ORDER TRAVERSAL*/
    public static void preOrderTraversal(TreeNode t)
    {
        if(t!=null)
        {
            System.out.println(t.data);
            if(t.left!=null)
            {
                preOrderTraversal(t.left);
            }
            if(t.right!=null)
            {
                preOrderTraversal(t.right);
            }
        }
    }
    /*POST-ORDER TRAVERSAL*/
    public static void postOrderTraversal(TreeNode t)
    {
        if(t!=null)
        {
            if(t.left!=null)
            {
                postOrderTraversal(t.left);
            }
            if(t.right!=null)
            {
                postOrderTraversal(t.right);
            }
            System.out.println(t.data);
        }
    }

    /*CREATE A BINARY SEARCH TREE*/
    public static TreeNode createMinimalBST(int array[], int start, int end)
    {
        if(end < start)
            return null;
        int mid = (start + end)/2;
        /*CREATE MAIN CENTRAL NODE*/
        TreeNode node = new TreeNode(array[mid]);
        /*SET LEFT CHILDREN*/
        node.setLeftChild(createMinimalBST(array, start, mid-1));
        /*SET RIGHT CHILDREN*/
        node.setRightChild(createMinimalBST(array, mid+1, end));
        return node;
    }

    /*CREATE A BINARY SEARCH TREE - HELPER FUNCTION*/
    public static TreeNode createMinimalBST(int array[])
    {
        return createMinimalBST(array, 0, array.length-1);
    }
    public void print()
    {
        BTreePrinter.printNode(this);
    }



}
