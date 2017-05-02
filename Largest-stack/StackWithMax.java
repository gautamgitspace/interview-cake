/**
 * Created by Gautam on 7/14/16.
 */

package Largest-stack;
import java.util.Stack;

public class StackWithMax extends Stack<Integer>
{
    Stack<Integer> s2;

    public StackWithMax()
    {
        s2 = new Stack<Integer>();
    }

    public void push(int value)
    {
        //compare value with integer.maxvalue, if less (obvious) push it to min stack
        if (value >= max())
        {
            s2.push(value);
            System.out.println("pushed: " + value);
        }
        //irrespective of anything, push it to main stack
        super.push(value);
    }

    public Integer pop()
    {
        //pop irrespective of anything from the main stack
        int value = super.pop();
        //if value lies in min stack, pop it from there too
        if (value == max())
        {
            s2.pop();
        }
        return value;
    }
    //return the top most element always
    public int max()
    {
        if (s2.isEmpty())
            return 0;
        else
            return s2.peek();
    }
}
