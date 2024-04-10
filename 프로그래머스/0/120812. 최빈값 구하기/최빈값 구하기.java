import java.util.*;
class Solution {
    public int solution(int[] array) {
        HashMap<Integer, Integer> hash = new HashMap<>();
        int max = array[0], cnt = 0;
        
        for(int i = 0; i<array.length; i++){
            hash.put(array[i], hash.getOrDefault(array[i], 0) + 1);
            if(hash.get(max) < hash.get(array[i])) max = array[i];
        }
        
        for(int i : hash.keySet()){
            if(hash.get(i) == hash.get(max)) cnt++;
        }
        
        return cnt > 1 ? -1 : max;
    }
}