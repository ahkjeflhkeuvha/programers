class Solution {
    boolean solution(String s) {
        int chk = 0;
        for(int i = 0; i<s.length(); i++){
            if(s.charAt(i) == 'p' || s.charAt(i) == 'P') chk++;
            else if(s.charAt(i) == 'y' || s.charAt(i) == 'Y') chk--;
        }
        return chk == 0 ? true : false;
    }
}