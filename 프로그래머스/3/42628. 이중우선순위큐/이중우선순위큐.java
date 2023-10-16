import java.util.Collections;
import java.util.Arrays;
import java.util.ArrayList;

class Solution {
    public int[] solution(String[] operations) {
        int[] answer = {0,0};
        ArrayList <Integer>list = new ArrayList<Integer>(10);
        
        for(int i = 0; i<operations.length; i++){
            String st[] = operations[i].split(" ");
            if(st[0].equals("I")) list.add(Integer.parseInt(st[1]));
            else if(st[0].equals("D") && st[1].equals("1")){
                Collections.sort(list);
                if(list.size() == 0) continue;
                else list.remove(list.size() - 1);
            }
            else if(st[0].equals("D") && st[1].equals("-1")){
                Collections.sort(list);
                if(list.size() == 0) continue;
                else list.remove(0);
            }   
        }
        Collections.sort(list);
        if(list.size() == 0) return answer;
        else {
            answer[0] = list.get(list.size() - 1);
            answer[1] = list.get(0);
        }
        
        return answer;
    }
}