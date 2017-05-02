package CTCI3_5;

import java.util.LinkedList;
import java.util.Queue;

/**
 * Created by Gautam on 8/15/16.
 */
public class Driver
{
    private static int randomInt(int n)
    {
        return (int) (Math.random() * n);
    }

    private static int randomIntInRange(int min, int max)
    {
        return randomInt(max + 1 - min) + min;
    }
    public static void main(String[] args)
    {
        /*INITIALIZE  MyQueue*/
        MyQueue my_queue = new MyQueue();

        /*INITIALIZE a REAL LINKED-LIST BASED QUEUE TO TEST AGAINST*/
        Queue<Integer> test_queue = new LinkedList<Integer>();

        for (int i = 0; i < 10; i++)
        {
            int choice = randomIntInRange(0, 10);

            System.out.println("CHOICE WAS: " + choice);
            if (choice <= 5)
            {
                /*ENQUEUE OPERATION*/

                int element = randomIntInRange(1, 10);
                test_queue.add(element);
                my_queue.addToInbox(element);

                System.out.println("Enqueued " + element);
            }
            else if(test_queue.size() > 0)
            {

                /*DEQUEUE OPERATION on both the Queues to TEST*/

                int top1 = test_queue.remove();
                int top2 = my_queue.dequeue();
                if (top1 != top2)
                {
                    /* ERROR CASE #1 */
                    System.out.println("FAILURE TYPE - DIFFERENT TOPS: " + top1 + ", " + top2);
                }
                System.out.println("Dequeued " + top1);
            }

            if (test_queue.size() == my_queue.size())
            {
                /* ERROR CASE #2 */
                if (test_queue.size() > 0 && test_queue.peek() != my_queue.peek())
                {
                    System.out.println("FAILURE TYPE - DIFFERENT TOP PEEKS: " + test_queue.peek() + ", " + my_queue.peek() + " ******");
                }
            }
            else
            {
                /* ERROR CASE #3 */
                System.out.println(" FAILURE TYPE - DIFFERENT SIZES ");
            }
        }
    }
}
