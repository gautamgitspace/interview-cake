package CTCI4_1;

import static CTCI4_1.TreeNode.inOrderTraversal;
import static CTCI4_1.TreeNode.postOrderTraversal;
import static CTCI4_1.TreeNode.preOrderTraversal;

/**
 * Created by Gautam on 8/16/16.
 */
public class BalancedBinaryTree
{
/*KEY - CHECK HEIGHT AT EACH NODE, RETURN 0 if balanced and -1 if not balanced*/
    static int checkHeight(TreeNode root)
    {
        /*BASE CASE*/
        if(root == null)
            return 0;
        /*COMPUTE HEIGHT DIFF AND SEE IF GT 1*/
        int leftHeight = checkHeight(root.left);
        int rightHeight = checkHeight(root.right);
        if(leftHeight == -1 || rightHeight == -1)
        {
            return -1;
        }

        int diffInHeight = leftHeight - rightHeight;
        if(Math.abs(diffInHeight) > 1)
        {
            return -1;
        }
        /*ELSE RETURN ACTUAL HEIGHT*/
        else
        {
            return 1 + Math.max(leftHeight,rightHeight);
        }
    }

    public static boolean isBalanced(TreeNode root)
    {
        if(checkHeight(root) == -1)
        {
            return false;
        }
        else
        {
            return true;
        }
    }

    public static void main(String[] args)
    {
        // Create balanced tree
        int[] array = {0, 1, 2, 3, 5, 6, 7, 8, 9, 10};
        TreeNode root = TreeNode.createMinimalBST(array);
        System.out.println("CALLING IN-ORDER");
        inOrderTraversal(root);
        System.out.println("CALLING PRE-ORDER");
        preOrderTraversal(root);
        System.out.println("CALLING POST-ORDER");
        postOrderTraversal(root);

        System.out.println("Is balanced? " + isBalanced(root));
        root.print();

        /*UNBALANCE*/
        root.insert(4);

        root.print();
        System.out.println("Is balanced? " + isBalanced(root));
    }

}

