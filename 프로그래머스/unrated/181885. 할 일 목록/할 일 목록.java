class Solution {
    public String[] solution(String[] todo_list, boolean[] finished) {
        int sum = 0, j = 0;
        for(int i = 0; i<todo_list.length; i++){
            if(finished[i] == false) sum++;
        }
        String[] answer = new String[sum];
        for(int i = 0; i<todo_list.length; i++){
            if(finished[i] == false){
                answer[j] = todo_list[i];
                j++;
            }
        }
        return answer;
    }
}