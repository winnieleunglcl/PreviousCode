package comp2011.ass2;

import java.util.Arrays;

/**
 * 
 * @author yixin cao (October 10, 2020)
 *
 * The heap data structure storing objects (using generics).
 * 
 * Again, we use an explicit variable key and use it for comparisons  
 * This a bad idea. See more at the comments of  {@code comp2011.lec8.BinarySearchTree}.
 */
public class Heap<T> {
    private static class Node<T> {
        int key;
        T obj;

        public Node(int key, T element) {
            this.key = key;
            this.obj = element;
        }

        public String toString() {
            return key + ": " + obj;
        }
    }

	private Node<T>[] data;
	int size;
	
    @SuppressWarnings("unchecked")
    public Heap(int capacity) {
    	data = new Node[capacity];
    	size = 0;
    }
    
    private void swap(int i, int j) {
        Node<T> temp = data[i];
        data[i] = data[j];
        data[j] = temp;
    }

    // the intuitive but slightly boring version.
    public void down(int p) {
        if (size < 2 * p + 2) return;
        int leftChild = p * 2 + 1;
        int rightChild = leftChild + 1;
        int largerChild = leftChild;
        // don't forget to check rightChild < size 
        if (rightChild < size && data[leftChild].key < data[rightChild].key)
            largerChild = rightChild;
        if (data[p].key >= data[largerChild].key) return;
        swap(p, largerChild);
        down(largerChild);
    }
    // the crisp version.
    public void downV2(int p) { 
        if (p * 2 + 2 > size) return;
        int larger = p * 2 + 1;
        if (larger + 1 < size && data[larger].key < data[larger+1].key) 
            larger++;
        if (data[p].key >= data[larger].key) return;
        swap(p, larger);
        downV2 (larger);
    }
    
    private void err(String message) {
        System.out.println("oops..." + message);
    }

    public T deleteMax() {
        if (size == 0) {err("downflow"); return null;}
        
        T ans = data[0].obj;
        data[0] = data[--size];
        iDown(0);
        return ans; 
    }
    public void up(int c) {
        if (c == 0) return;
        int p = (c - 1) / 2;
        if (data[c].key <= data[p].key) return;
        swap(c, p);
        up(p);
    }
    public void insert(int key, T x) {
        // a more friendly way is to double the size of arr
        if (size == data.length) {err("overflow"); return;}
        data[size] = new Node<T>(key, x);
        iUp(size++);
    }

    // Tasks: iterative versions of bubble down and bobble up.

    // The running time of iDown is O(logn).
    public void iDown(int p) {
        if (p * 2 + 2 > size) return;
        int leftChild = p * 2 + 1;
        int rightChild = leftChild + 1;
        int largerChild = leftChild;
        if (rightChild < size && data[leftChild].key < data[rightChild].key) largerChild = rightChild;
        if (data[p].key >= data[largerChild].key) return;

        int swap = 0;
        while(data[p].key < data[largerChild].key){
            swap++;
            if (largerChild == (size-2)) {
                swap(p, size-2);
                break;
            }
            leftChild = largerChild * 2 + 1;
            rightChild = leftChild + 1;
            largerChild = leftChild;
            if (rightChild < size && data[leftChild].key < data[rightChild].key) largerChild = rightChild;
            if (data[p].key > data[largerChild].key){
                swap(p,(largerChild-1)/2);
                break;
            }
        }
        if (swap>1){
            int location = p;
            leftChild = location * 2 + 1;
            rightChild = leftChild + 1;
            largerChild = leftChild;
            if (rightChild < size && data[leftChild].key < data[rightChild].key) largerChild = rightChild;
            for (int i=1; i<swap; i++){
                swap(location,largerChild);
                location = largerChild;
                leftChild = largerChild * 2 + 1;
                rightChild = leftChild + 1;
                largerChild = leftChild;
                if (rightChild < size && data[leftChild].key < data[rightChild].key) largerChild = rightChild;
            }
        }
    }

    // The running time of iUp is O(logn).
    public void iUp(int c) {
        if (c == 0) return;
        int parentNode = (c-1)/2;
        if (data[c].key <= data[parentNode].key) return;
        int swap = 0;
        while(data[c].key > data[parentNode].key){
            swap++;
            if (parentNode == 0) {
                swap(c, 0);
                break;
            }
            parentNode = (parentNode-1)/2;
            if (data[c].key < data[parentNode].key){
                swap(c,(c-1)/2);
                break;
            }
        }
        if (swap>1){
            int location = c;
            parentNode = (c-1)/2;
            for (int i=1; i<swap; i++){
                swap(location,parentNode);
                location = parentNode;
                parentNode = (location-1)/2;
            }
        }
    }
    
    // =========================
    // Codes below are for testing.
    public String toString() {
        return Arrays.toString(Arrays.copyOfRange(data, 0, size));
    }

    static class Student {
        int id;
        String name;

        public Student(int id, String name) {
            this.id = id;
            this.name = name;
        }

        public String toString() {
            return name;
        }
    }

    public static void main(String[] args) {
        Heap<Student> heap = new Heap<Student>(20);
        heap.insert(214, new Student(214, "Chan Eason"));
        heap.insert(562, new Student(562, "Cheung Jacky"));
        heap.insert( 83, new Student( 83, "Ho Denise"));
        heap.insert(115, new Student(115, "Joey Yung"));
        heap.insert( 97, new Student( 97, "Andy Lau"));
        heap.insert(722, new Student(722, "Leung Gigi"));
        heap.insert(398, new Student(398, "Tang Gloria"));
        heap.insert(798, new Student(798, "Mickey"));
        heap.insert(408, new Student(408, "Teddy"));
        heap.insert(199, new Student(199, "Tse Kay"));
        heap.insert(337, new Student(337, "McDull"));
        System.out.println(heap);
        heap.deleteMax();
        System.out.println("=====================");
        System.out.print(heap);
    }
}

