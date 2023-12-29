import java.util.*;
class Solution {
    public int solution(int[] array, int n) {
        int answer = 0, min;
        Arrays.sort(array);
        int arr[] = new int[array.length];
        for(int i = 0; i<array.length; i++){
            min = array[i] - n;
            if(min < 0) min *= -1;
            arr[i] = min;
        }
        min = 100;
        System.out.println(Arrays.toString(arr));
        for(int i = 0; i<array.length; i++){
            if(min > arr[i]) {
                min = arr[i];
                answer = array[i];
            }
        }
        return answer;
    }
}