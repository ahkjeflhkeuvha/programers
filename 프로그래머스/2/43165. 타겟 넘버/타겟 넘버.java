import java.util.*;

class Solution {
    static List<Integer> list;
    static int answer = 0;
    
    public int solution(int[] numbers, int target) {
        list = new ArrayList<>();
        dfs(numbers, 0, target, 0);
        return answer;
    }
    
    static void dfs(int[] numbers, int idx, int target, int sum){
        int ans = sum;
        
        if(idx == numbers.length){
            if(ans == target) answer++;
        }
        else {
            dfs(numbers, idx + 1, target, ans + numbers[idx]);
            dfs(numbers, idx + 1, target, ans - numbers[idx]);
        }
    }
}