import java.util.*;
class Solution {
    public int[] solution(int[] answers) {
        ArrayList<Integer> list = new ArrayList<>();
        int[] no_1 = {1, 2, 3, 4, 5};
        int[] no_2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] no_3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        int x = 0, y = 0, z = 0, no_x = 0, no_y = 0, no_z = 0, max = 0;
        for(int i = 0; i<answers.length; i++, x++, y++, z++){
            if(x >= no_1.length) x = 0;
            if(y >= no_2.length) y = 0;
            if(z >= no_3.length) z = 0;
            
            if(answers[i] == no_1[x]) no_x++;
            if(answers[i] == no_2[y]) no_y++;  
            if(answers[i] == no_3[z]) no_z++;
        }
        
        max = Math.max(no_x, no_y);
        max = Math.max(max, no_z);
        
        if(no_x == max) list.add(1);
        if(no_y == max) list.add(2);
        if(no_z == max) list.add(3);
        
        int n = 0;
        int[] answer = new int[list.size()];
        for(int i : list) answer[n++] = i;
        return answer;
    }
}