import java.util.*;
class Solution {
    public int solution(int[] array) {
        int answer = array[0], max = 1, temp = 0;
        HashMap<Integer, Integer> hash = new HashMap<Integer, Integer>();
        for(int i = 0; i<array.length; i++){
            if(hash.containsKey(array[i])){
                int val = hash.get(array[i]);
                hash.put(array[i], ++val); 
                if(val > max) {
                    answer = array[i];
                    max = val;
                }
            }
            else {
                hash.put(array[i], 1);
            }
        }
        Set<Integer> keySet = hash.keySet();        
        for (Integer key : keySet) {            
            if(hash.get(key) == max) temp++;
            if(temp > 1) answer = -1;
            System.out.println(key + ":" + hash.get(key));
        }
        return answer;
    }
}