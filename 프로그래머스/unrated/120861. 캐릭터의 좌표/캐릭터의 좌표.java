class Solution {
    public int[] solution(String[] keyinput, int[] board) {
        int[] answer = new int[2];
        for(String str : keyinput){
            if(str.equals("left")) answer[0]--;
            else if(str.equals("right")) answer[0]++;
            else if(str.equals("up")) answer[1]++;
            else if(str.equals("down")) answer[1]--;
            
            if(Math.abs(answer[0]) > (board[0]-1)/2) answer[0] = answer[0] > 0 ? (board[0]-1)/2 : (board[0]-1)/2*-1;
            if(Math.abs(answer[1]) > (board[1]-1)/2) answer[1] = answer[1] > 0 ? (board[1]-1)/2 : (board[1]-1)/2*-1;
        }
        return answer;
    }
}