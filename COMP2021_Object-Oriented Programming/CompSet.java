package hk.edu.polyu.comp.comp2021.assignment4.compset;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class CompSet<T> {

    /** Each CompSet uses at most 1023 buckets.   */
    private static final int NUBMER_OF_BUCKETS = 1023;

    /** An array of buckets as the storage for each set. */
    private List<T>[] storage;

    public CompSet() {
        // Add missing code here
        this.storage = new List[NUBMER_OF_BUCKETS];
        for (int i = 0; i < NUBMER_OF_BUCKETS; i++) {
            this.storage[i] = Arrays.asList();
        }
    }

    /**
     * Initialize 'this' with the unique elements from 'elements'.
     * Throw IllegalArgumentException if 'elements' is null.
     */
    public CompSet(List<T> elements) {
        // Add missing code here
        if(elements.equals(null)){
            throw new IllegalArgumentException();
        }
        this.storage = new List[NUBMER_OF_BUCKETS];
        int i=0;
        for (T element : elements){
            this.storage[i] = Arrays.asList(elements.get(i));
            i++;
        }
        for (; i < NUBMER_OF_BUCKETS; i++) {
            this.storage[i] = Arrays.asList();
        }
    }

    /**
     * Get the total number of elements stored in 'this'.
     */
    public int getCount() {
        // Add missing code here
        if (this.isEmpty()){return 0;}
        int count = 0;
        for (int i = 0; i < NUBMER_OF_BUCKETS; i++) {
            if (!this.storage[i].isEmpty()) {
                count++;
            }
        }
        return count;
    }

    public boolean isEmpty() {
        // Add missing code here
        boolean flag = true;
        for (int i = 0; i < NUBMER_OF_BUCKETS; i++) {
            if (!this.storage[i].isEmpty()){
                flag = false;
                break;
            }
        }
        return flag;
    }

    /**
     * Whether 'element' is contained in 'this'?
     */
    public boolean contains(T element) {
        // Add missing code here
        boolean flag = false;
        for (int i = 0; i < NUBMER_OF_BUCKETS; i++) {
            for (T e : this.storage[i]) {
                if (e.equals(element)) {
                    flag = true;
                    break;
                }
            }
            if(flag) break;
        }
        return flag;
    }

    /**
     * Get all elements of 'this' as a list.
     */
    public List<T> getElements() {
        // Add missing code here
        List<T> list = new ArrayList<T>();;
        for (int i = 0; i < NUBMER_OF_BUCKETS; i++) {
            if (!this.storage[i].isEmpty()){
                list.add(this.storage[i].get(0));
            }
        }
        return list;
    }

    /**
     * Add 'element' to 'this', if it is not contained in 'this' yet.
     * Throw IllegalArgumentException if 'element' is null.
     */
    public void add(T element) {
        // Add missing code here
        if(element==null){
            throw new IllegalArgumentException();
        }
        if (!this.contains(element)){
            for (int i = 0; i < NUBMER_OF_BUCKETS; i++) {
                if (this.storage[i].isEmpty()){
                    this.storage[i] = Arrays.asList(element);
                    break;
                }
            }
        }
    }

    /**
     * Two CompSets are equivalent is they contain the same elements.
     * The order of the elements inside each CompSet is irrelevant.
     */
    public boolean equals(Object other){
        // Add missing code here
        if (other==null)return false;
        return this.getElements().containsAll(((CompSet<?>) other).getElements()) && ((CompSet<?>) other).getElements().containsAll(this.getElements());
    }

    /**
     * Remove 'element' from 'this', if it is contained in 'this'.
     * Throw IllegalArgumentException if 'element' is null.
     */
    public void remove (T element) {
        // Add missing code here
        if(element==null){
            throw new IllegalArgumentException();
        }
        if (this.contains(element)){
            for (int i = 0; i < NUBMER_OF_BUCKETS; i++) {
                if (this.storage[i].contains(element)) {
                    this.storage[i] = Arrays.asList();
                    break;
                }
            }
        }
    }

    //========================================================================== private methods

    private int getIndex(T element) {
        return element.hashCode() % NUBMER_OF_BUCKETS;
    }

}


