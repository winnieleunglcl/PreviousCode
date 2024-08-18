package comp2011.ass2;

import java.util.Arrays;

/**
 * 
 * @author yixin cao (November 10, 2020)
 *
 * Find the k numbers with most occurrences from an array of n integers.
 * 
 */
public class MostCommonElements {

    // The running time of mostFrequent is O(n^2).
    public static int[] mostFrequent(int[] a, int k) {
        int length = a.length;

        //sort the array in increasing order
        for (int i=0; i<length-1; i++){
            for (int j=0; j<length-i-1; j++){
                if (a[j]>a[j+1]){
                    int temp = a[j];
                    a[j] = a[j+1];
                    a[j+1] = temp;
                }
            }
        }

        //initialize an array to store each number's occurrence (must be 1 for each element)
        int[] countOccurrence = new int[length];
        for (int i=0; i<length; i++){
            countOccurrence[i] = 1;
        }

        //count real occurrence of each element by removing duplicate ones
        for (int i = 0; i < length; i++) {
            for (int j=i+1; j < length; j++){
                if (a[i] == a[j] && countOccurrence[j]!=0){
                    countOccurrence[i]++;
                    countOccurrence[j] = 0;
                }
            }
        }

        //find most occurrence's value
        int max = 0;
        for (int i=0; i<length; i++){
            if(max<countOccurrence[i]){
                max = countOccurrence[i];
            }
        }

        int [] result = new int[k];
        boolean flag = false;

        for (int i=0; i<k; i++){
            for (int j=0; j<length; j++){
                if(countOccurrence[j] == max){
                    result[i] = a[j];
                    countOccurrence[j] = 0;
                    flag = true;
                    break;
                }
                flag = false;
            }
            //if changing most occurrence's value is needed
            if (!flag){
                max = 0;
                for (int j=0; j<length; j++){
                    if(max<countOccurrence[j]){
                        max = countOccurrence[j];
                    }
                }
                for (int j=0; j<length; j++){
                    if(countOccurrence[j] == max){
                        result[i] = a[j];
                        countOccurrence[j] = 0;
                        flag = true;
                        break;
                    }
                    flag = false;
                }
            }
        }
        return result;
    }
    
    public static void main(String[] args) {
        int[] a = {12, 35, 1, 10, 35, 1, 19, 49};
        System.out.println(Arrays.toString(mostFrequent(a, 3)));
    }

}
