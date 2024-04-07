import java.util.*;
class Solution {
    public int[] solution(int[] answers) {
        ArrayList<Integer> list = new ArrayList<>();
        int[] no_1 = {1, 2, 3, 4, 5};
        int[] no_2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] no_3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        int no_x = 0, no_y = 0, no_z = 0, max = 0;
        for(int i = 0; i<answers.length; i++){   
            if(answers[i] == no_1[i%no_1.length]) no_x++;
            if(answers[i] == no_2[i%no_2.length]) no_y++;  
            if(answers[i] == no_3[i%no_3.length]) no_z++;
        }
        
        max = Math.max(no_x, no_y);
        max = Math.max(max, no_z);
        
        if(no_x == max) list.add(1);
        if(no_y == max) list.add(2);
        if(no_z == max) list.add(3);

        return list.stream().mapToInt(i->i.intValue()).toArray();
    }
}