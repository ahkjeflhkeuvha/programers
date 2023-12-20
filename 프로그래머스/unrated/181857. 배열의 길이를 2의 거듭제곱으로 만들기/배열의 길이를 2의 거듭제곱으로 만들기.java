import java.util.*;
class Solution {
    public int[] solution(int[] arr) {
        int length = 1;
        while(true) {
            if(length >= arr.length) break;
            length *= 2;
        }
        return Arrays.copyOf(arr, length);
    }
}