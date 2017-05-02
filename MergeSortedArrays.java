package CTCI11_1;

/**
 * Created by Gautam on 8/19/16.
 */
public class MergeSortedArrays
{
    public static void merge(int a[], int b[], int lastA, int lastB)
    {
        int indexA = lastA - 1;
        int indexB = lastB - 1;
        int indexResultant = lastA + lastB - 1;
        while(indexB>=0)
        {
            if(indexA >= 0 && a[indexA] > b[indexB])
            {
                a[indexResultant] = a[indexA];
                indexA--;
            }
            else
            {
                a[indexResultant] = b[indexB];
                indexB--;
            }
            indexResultant--;
        }
    }
    public static void main(String args[])
    {
        int a[] = {1,13,65,57,0,0,0,0,0,0,0,0,0};
        int b[] = {6,7,45,59};
        int lastA = 4;
        int lastB = 4;
        merge(a,b,lastA,lastB);
        StringBuilder stringBuilder = new StringBuilder();
        for(int v : a)
        {
            stringBuilder.append(v + ", ");
        }
        System.out.println(stringBuilder);
    }
}
