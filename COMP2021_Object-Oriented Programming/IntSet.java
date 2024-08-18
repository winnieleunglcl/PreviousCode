package hk.edu.polyu.comp.comp2021.assignment2.intset;

import com.sun.deploy.util.StringUtils;

import java.util.Arrays;

public class IntSet {

    public static final int INDEX_NOT_FOUND = -1;

    // Internal storage of the set.
    private int[] storage;
    // Maximum number of integers stored in the set.
    private int count;

    public IntSet(int size) {
        this.count = size;
        this.storage = new int[size];
        for (int i=0; i<size; i++){
            this.storage[i] = -1;
        }
    }

    public boolean isEmpty() {
        int count = 0;
        for (int i=0; i<this.count; i++){
            if (this.storage[i]!=-1){
                count++;
            }
        }
        if (count == 0){
            return true;
        }
        return false;
    }

    public boolean isFull() {
        int count = 0;
        for (int i=0; i<this.count; i++){
            if (this.storage[i]!=-1){
                count++;
            }
        }
        if (count == this.count){
            return true;
        }
        return false;
    }

    public void add(int x) {
        int index = -1;
        for (int i=0; i<this.count; i++){
            if (this.storage[i]==x){
                index = i;
                break;
            }
        }
        if (index == -1){
            for (int i=0; i<this.count; i++) {
                if (this.storage[i]==-1){
                    this.storage[i] = x;
                    break;
                }
            }
        }
    }

    public void remove(int x) {
        for (int i=0; i<this.count; i++){
            if (this.storage[i]==x){
                this.storage[i] = -1;
                break;
            }
        }
    }

    public boolean has(int x) {
        for (int i=0; i<this.count; i++){
            if (this.storage[i]==x){
                return true;
            }
        }
        return false;
    }

    public IntSet union(IntSet other) {
        IntSet U = new IntSet(this.count+other.count);
        int mid = this.count;
        for (int i=0; i<this.count; i++){
            U.storage[i] = this.storage[i];
        }
        for (int i=0; i<other.count; i++){
            U.storage[mid] = other.storage[i];
            mid++;
        }
        return U;
    }

    public IntSet intersection(IntSet other) {
        IntSet I = new IntSet(this.count);
        int tail = 0;
        for (int i=0; i<this.count; i++){
            for (int j=0; j<other.count; j++){
                if (this.storage[i]==other.storage[j]){
                    I.storage[tail] = this.storage[i];
                    tail++;
                }
            }
        }
        return I;
    }

    public String toString() {
        String result = "{";
        for (int i=0; i<this.count; i++){
            if (this.storage[i]!=-1){
                result += this.storage[i];
            }
            if (i==this.count-1||this.storage[i+1]==-1){
                break;
            }
            result += ",";
        }
        return result+"}";
    }

    public boolean isEqualTo(IntSet set2) {
        int count=0, size=0;
        for (int i=0; i<this.count; i++){
            if (this.storage[i] != -1){
                    size++;
            }
        }
        for (int i=0; i<this.count; i++){
            for (int j=0; j<set2.count; j++){
                if (this.storage[i] != -1 & this.storage[i]==set2.storage[j]){
                    count++;
                }
            }
        }
        if (count == size){
            return true;
        }
        return false;
    }

    // ==================================


}
