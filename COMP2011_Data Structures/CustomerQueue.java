package comp2011.ass1;

import comp2011.lec4.LinkedList;

/**
 * @author yixin cao (October 1, 2020)
 * <p>
 * A simulation of the queue waiting at a cashier.
 */
public class CustomerQueue {
    private LinkedList<String> list;

    public CustomerQueue() {
        list = new LinkedList<String>();
    }

    public boolean isEmpty() {
        return (list.isEmpty());
    }

    public void enqueue(String s) {
        list.insertLast(s);
    }

    public String dequeue() {
        return (list.removeFirst());
    }

    public String toString() {
        return null;
    }

    public CustomerQueue[] split(int k) {
        int index = 0;
        boolean condition = true;
        String temp;
        CustomerQueue[] customerQueues = new CustomerQueue[k];
        while (true) {
            temp = list.removeFirst();
            if (temp == null) {
                return customerQueues;
            }
            if (condition) {
                customerQueues[index] = new CustomerQueue();
            }
            customerQueues[index].enqueue(temp);
            index++;
            if (index == k) {
                index = 0;
                condition = false;
            }
        }
    }

    public static void main(String[] args) {
        CustomerQueue queue = new CustomerQueue();
        System.out.println("There is no customer waiting at the cashier: " + queue.isEmpty());
        queue.enqueue("Eason");
        System.out.println("Customer(s) waiting: ");
        System.out.println(queue.list);
        System.out.println("There is no customer waiting at the cashier: " + queue.isEmpty());
        queue.enqueue("Denise");
        queue.enqueue("Jennifer");
        queue.enqueue("Joey");
        queue.enqueue("Kay");
        System.out.println("Customer(s) waiting: ");
        System.out.println(queue.list);
        System.out.println("Customer left: " + queue.dequeue());
        queue.enqueue("Cheung");
        queue.enqueue("Winnie");
        queue.enqueue("Mickey");
        queue.enqueue("Teddy");
        queue.enqueue("Peppa");
        System.out.println("Customer left: " + queue.dequeue());
        System.out.println("Customer(s) waiting: ");
        System.out.println(queue.list);
        CustomerQueue[] queues = queue.split(3);
        System.out.println("k queue(s) is/are working, the situation is:");
        for (CustomerQueue q : queues) System.out.println(q.list);
    }
}