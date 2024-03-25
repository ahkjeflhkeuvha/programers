import java.util.*;
class Solution {
    public int solution(int[] date1, int[] date2) {
        Date FirDate = new Date(date1[0], date1[1], date1[2]);
        Date SecDate = new Date(date2[0], date2[1], date2[2]);
        
        return FirDate.compareTo(SecDate) < 0 ? 1 : 0;
    }
}