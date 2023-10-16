import java.util.*;
class Solution
{
    public int solution(int []A, int []B)
    {
        int answer = 0;
        ArrayList<Integer> Alist = new ArrayList<Integer>();
        ArrayList<Integer> Blist = new ArrayList<Integer>();
        
        for(int i = 0; i<A.length; i++){
            Alist.add(A[i]);
            Blist.add(B[i]);
        }
        Collections.sort(Alist);
        Collections.sort(Blist, Collections.reverseOrder());
        
        for(int i = 0; i<Alist.size(); i++){
            answer += (Alist.get(i) * Blist.get(i));
        }
        return answer;
    }
}