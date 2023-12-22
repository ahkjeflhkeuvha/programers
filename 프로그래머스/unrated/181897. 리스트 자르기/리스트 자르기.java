import java.util.*;
class Solution {
    public int[] solution(int n, int[] slicer, int[] num_list) {
        ArrayList <Integer> list = new ArrayList<>();
        int st = 0, en = 0, pl = 0;
        switch(n){
            case 1: st = 0; en = slicer[1]; pl = 1; break;
            case 2: st = slicer[0]; en = num_list.length - 1; pl = 1; break;
            case 3: st = slicer[0]; en = slicer[1]; pl = 1; break;
            case 4: st = slicer[0]; en = slicer[1]; pl = slicer[2]; break;
        }
        for(int i = st; i <= en; i += pl) list.add(num_list[i]);

        int answer[] = new int[list.size()];
        int i = 0;
        for(int res : list) answer[i++] = res;
        return answer;
    }
}