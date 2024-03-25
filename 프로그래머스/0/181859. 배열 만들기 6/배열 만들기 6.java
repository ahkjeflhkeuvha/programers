import java.util.Stack;
class Solution {
    public int[] solution(int[] arr) {
        Stack <Integer> stack = new Stack<>();
        
        for(int i : arr){
            if(!stack.isEmpty() && i == stack.peek()) stack.pop();
            else stack.push(i);
        }
        
        return stack.isEmpty() ? new int[] {-1} : stack.stream().mapToInt(i -> i).toArray();
    }
}