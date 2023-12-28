import java.util.*;
class Solution {
    public int solution(int[] arr) {
        int answer = 0, check = 0;
        int before[], after[];
        while(true){
            before = Arrays.copyOf(arr, arr.length);
            for(int i = 0; i<arr.length; i++){
                if(arr[i] >= 50 && arr[i]%2 == 0) arr[i] = arr[i] / 2;
                else if(arr[i] < 50 && arr[i]%2 == 1) arr[i] = (arr[i] * 2) + 1;
            }
            after = Arrays.copyOf(arr, arr.length);
            for(int j = 0; j<arr.length; j++) {
                if(before[j] == after[j]) {
                    if(j == arr.length -1){
                        check++;
                        break;
                    }
                }
                else break;
            }
            if(check != 0) break;
            answer++;
        }
        return answer;
    }
}