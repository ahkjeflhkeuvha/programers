import java.util.ArrayList;
class Solution {
    public int[] solution(int[] arr, int[][] intervals) {
        ArrayList <Integer> list = new ArrayList<>();
        for(int i = 0; i<intervals.length; i++)
            for(int j = intervals[i][0]; j< intervals[i][1] + 1; j++)
                list.add(arr[j]);
        
        int n = 0;
        int[] answer = new int[list.size()];
        for(int i : list)
            answer[n++] = i;
        return answer;
    }
}