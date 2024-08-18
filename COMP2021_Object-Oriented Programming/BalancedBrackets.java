package hk.edu.polyu.comp.comp2021.assignment1;

import java.util.Stack;

public class BalancedBrackets {

    public static boolean isBalanced(String str) {

        //if the total number of opening brackets != that of closing brackets (=length%2 != 0)
        //the string is impossible to be balanced
        if (str.length()%2 != 0){
            return false;
        }

        //make sure the string contains only six characters
        char[] copyStr = str.toCharArray();
        for (char c: copyStr){
            if (!(c=='(' || c=='[' || c=='{' || c==')' || c==']' || c=='}')){
                return false;
            }
        }

        //create a stack data structure to push and pop the opening brackets
        Stack<Character> stack = new Stack<>();
        for (int i=0; i<str.length(); i++){
            char currentChar = str.charAt(i);
            //if the current character is a opening bracket, push it into the stack
            if (currentChar == '(' || currentChar == '[' || currentChar == '{'){
                stack.push(currentChar);
            }
            //if the current character is a closing bracket, check if the top of the stack is the corresponding opening bracket
            //if not, then the string must not be balanced.
            else if (currentChar == ')'){
                if (stack.pop() != '('){
                    return false;
                }
            }
            else if (currentChar == ']'){
                if (stack.pop() != '['){
                    return false;
                }
            }
            else{
                if (stack.pop() != '{'){
                    return false;
                }
            }
        }

        //if stack is empty, the string is balanced.
        return stack.isEmpty();
    }
}
