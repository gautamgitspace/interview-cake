/**
 * Created by Gautam on 7/14/16.
 */

public class TestMethod
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
        StackWithMax stack2 = new StackWithMax();
        for (int i = 0; i < 15; i++)
        {
            int value = randomIntInRange(0, 100);
            stack2.push(value);
            System.out.print(value + ", ");
        }
        System.out.println('\n');
        for (int i = 0; i < 15; i++)
        {
            int index=i;
            System.out.println("Popped[" + ++index +"]" + stack2.pop());
            if(!stack2.isEmpty())
                System.out.println("New max is " +  stack2.max());
            else
                System.out.println("Stack Empty");
        }
    }
}
