package comp2011.ass2;

import java.util.Arrays;

/**
 * 
 * @author yixin cao (November 10, 2020)
 *
 * Find the k largest elements from an array of n integers.
 * 
 * Use two different algorithms to do this task.
 */
public class LargestK {

    // The running time of m1 is O(kn) --> O(n).
    public static int[] m1(int[] a, int k) {
        int[] b = a.clone();
        int[] result = new int[k];
        for (int i=0; i<k; i++){
            int max = b[0];
            int index = 0;
            for (int j=1; j<b.length; j++){
                if (b[j]>max){
                    max = b[j];
                    index = j;
                }
            }
            b[index] = 0;
            result[i] = max;
        }
        return result;
    }
    
    // The running time of m2 is O(k+n^2) --> O(n^2).
    public static int[] m2(int[] a, int k) {
        int[] result = new int[k];
        for (int i=0; i<a.length-1; i++){
            for (int j=0; j<a.length-i-1; j++){
                if (a[j]<a[j+1]){
                    int temp = a[j];
                    a[j] = a[j+1];
                    a[j+1] = temp;
                }
            }
        }
        for (int i=0; i<k; i++){
            result[i] = a[i];
        }
        return result;
    }
    
    public static void main(String[] args) {
        int[] a = {12, 35, 1, 10, 35, 1, 19, 49};
        System.out.println(Arrays.toString(m1(a, 3)));
        System.out.println(Arrays.toString(m2(a, 4)));
    }

}
