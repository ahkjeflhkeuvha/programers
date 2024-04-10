import java.util.*;

public class Solution {
    public Stack<Integer> solution(int []arr) {
        Stack<Integer> stack = new Stack<>();
        stack.add(arr[0]);
        for(int i = 0; i<arr.length; i++){
            if(arr[i] != stack.peek()) stack.add(arr[i]);
        }

        return stack;
    }
}