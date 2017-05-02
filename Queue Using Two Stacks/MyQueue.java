package CTCI3_5;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

import static javafx.scene.input.KeyCode.T;

/**
 * Created by Gautam on 8/15/16.
 */
public class MyQueue
{

    /*STACK TO WHICH WE PUSH THE NEW INCOMING ELEMENTS*/
    Stack<Integer> inbox;
    /*STACK FROM WHICH WE POP OR DEQUEUE*/
    Stack<Integer> outbox;

    MyQueue()
    {
        System.out.println("DEF CONS");
        inbox = new Stack<Integer>();
        outbox= new Stack<Integer>();
    }
    /*GET SIZE METHOD*/
    public Integer size()
    {
        return inbox.size() + outbox.size();
    }
    /*PEEK METHOD*/
    public Integer peek()
    {
        shiftStacks();
        return outbox.peek();
    }

    /*DEQUEUE METHOD*/
    public Integer dequeue()
    {
        shiftStacks();
        return outbox.pop();
    }
    /*ENQUEUE METHOD*/

    public void addToInbox(Integer value)
    {
        inbox.push(value);
    }

    /*SHIFT STACKS LOGIC*/
    private void shiftStacks()
    {
        if(outbox.isEmpty())
        {
            while(!inbox.isEmpty())
            {
                outbox.push(inbox.pop());
            }
        }
    }

}
