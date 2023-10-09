class Solution {
    public String solution(String rsp) {
        String answer = "";
        for(int i = 0; i<rsp.length(); i++){
            switch((rsp.charAt(i)-47)/3){
                case 0: answer += '5'; break;
                case 1: answer += '0'; break;
                default: answer += '2'; break;
            }
        }
        return answer;
    }
}