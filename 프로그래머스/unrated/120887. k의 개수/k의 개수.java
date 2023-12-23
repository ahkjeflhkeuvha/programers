class Solution {
    public int solution(int i, int j, int k) {
        int answer = 0;
        String strK = Integer.toString(k);
        for(int start = i; start<=j; start++){
            String[] str = Integer.toString(start).split("");
            for(int strLen = 0; strLen<str.length; strLen++){
                if(str[strLen].equals(strK)) answer++;
            }
        }
        return answer;
    }
}