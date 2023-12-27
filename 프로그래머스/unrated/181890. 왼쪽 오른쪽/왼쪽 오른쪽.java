class Solution {
    public String[] solution(String[] str_list) {
        int start = 0, end = 0;
        for(int i = 0; i<str_list.length; i++) {
            if(str_list[i].matches("r")) {
                start = i+1; end = str_list.length;
                break;
            }
            else if(str_list[i].matches("l")){
                start = 0; end = i;
                break;
            }
        }
        String[] answer = new String[end - start];
        int n = 0;
        for(int i = start; i < end; i++) answer[n++] = str_list[i];
        return answer;
    }
}