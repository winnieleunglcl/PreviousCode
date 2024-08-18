package comp2011.ass2;

import java.util.Arrays;

/**
 * 
 * @author yixin cao (November 10, 2020)
 *
 * Use a maximum tree (introduced in Lecture 9) to sort an array.
 * 
 * To make it simple, I don't use generics here.
 * It's easy to revise it to use generics.
 */
public class MaxTree {
    private class Node {
        int element;
        public Node leftChild, rightChild;
        public Node(int element) { this.element = element; }
        public String toString() { return String.valueOf(element); }
    }
    Node root;
    
    // Build a maximum tree out of an array.
    public MaxTree(int[] a) {
        int n = a.length;
        Node[] nodes = new Node[n];
        for (int i = 0; i < n; i++) {
            nodes[i] = new Node(a[i]);
        }
        while (n > 1) {
            for (int i = 0; i < n / 2; i++) {
                int max = Math.max(nodes[i * 2].element, nodes[i * 2 + 1].element);
                Node newNode = new Node(max);
                newNode.leftChild = nodes[i * 2];
                newNode.rightChild = nodes[i * 2 + 1];
                nodes[i] = newNode; // why it's safe to resue the space?
            }
            // n might be odd.
            if (n % 2 != 0)  {
                nodes[n/2] = new Node(nodes[n - 1].element);
                nodes[n/2].leftChild = nodes[n - 1];
            }
            
            n = (n + 1) / 2;
        }
        root = nodes[0];
    }

    // imlement this
    // The running time of deleteMax is O(logn).
    public int deleteMax() {
        int max = root.element;
        rearrangeTree(root, max);

        int left = root.leftChild != null ? root.leftChild.element : Integer.MIN_VALUE;
        int right = root.rightChild != null ? root.rightChild.element : Integer.MIN_VALUE;

        root.element = Math.max(left, right);

        return max;
    }

    public void rearrangeTree(Node root, int max) {
        if (root.leftChild == null && root.rightChild != null) {
            rearrangeTree(root.rightChild, max);
        }
        if (root.rightChild == null && root.leftChild != null) {
            rearrangeTree(root.leftChild, max);
        }
        if (root.rightChild != null && root.leftChild != null) {
            if (root.leftChild.element > root.rightChild.element)
                rearrangeTree(root.leftChild, max);
            else
                rearrangeTree(root.rightChild, max);

        }
        if (root.element == max && root.leftChild == null && root.rightChild == null) {
            root.element = Integer.MIN_VALUE;
        }
        if (root.leftChild == null && root.rightChild != null) {
            root.element = root.rightChild.element;
        }
        if (root.rightChild == null && root.leftChild != null) {
            root.element = root.leftChild.element;
        }
        if (root.rightChild != null && root.leftChild != null) {
            root.element = Math.max(root.leftChild.element, root.rightChild.element);
        }
        if (root.leftChild != null && root.leftChild.element == Integer.MIN_VALUE) {
            root.leftChild = null;
        }
        if (root.rightChild != null && root.rightChild.element == Integer.MIN_VALUE) {
            root.rightChild = null;
        }
    }

    public static void treeSort(int[] a) {
	    MaxTree tree = new MaxTree(a);
	    for (int i = a.length; i > 0 ; i--) {
	        a[i - 1] = tree.deleteMax();
	    }
	}

	public static void main(String[] args) {
//      int size = 10;
//      int[] a = new int[size];
//      SecureRandom random = new SecureRandom();
//      for (int i = 0; i < size; i++)
//          a[i] = random.nextInt(size);

        int[] a = {3, 2, 6, 13, 8, 4, 10, 7, 14, 11, 12, 5, 9};
        System.out.println(Arrays.toString(a));
        treeSort(a);
        System.out.println(Arrays.toString(a));
	}
}
