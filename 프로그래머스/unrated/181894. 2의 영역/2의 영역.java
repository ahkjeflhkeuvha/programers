import java.util.*;
class Solution {
    public int[] solution(int[] arr) {
        int stridx = 100000, endidx = 0;
        for(int i = 0; i<arr.length; i++){
            if(arr[i] == 2){
                stridx = Math.min(stridx, i);
                endidx = Math.max(endidx, i);
            }
        }
        if(stridx <= endidx) return Arrays.copyOfRange(arr, stridx, endidx + 1);
        else return new int[]{-1};
    }
}