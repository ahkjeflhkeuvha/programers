class Solution {
    public String solution(String new_id) {
        String answer = "";
        answer = new_id.toLowerCase();
        answer = answer.replaceAll("[^\\w\\-_.]*", "");
        answer = answer.replaceAll("\\.{2,}", ".");
        answer = answer.replaceAll("^[.]|[.]$", "");
        answer = answer.length() == 0 ? "a" : answer;
        
        if(answer.length() >= 16) answer = answer.substring(0, 15).replaceAll("^[.]|[.]$", "");
        
        if(answer.length() <= 2) {
            char c = answer.charAt(answer.length() - 1);
            
            for(int i = 0; i<=3-answer.length(); i++){
                answer += c;
            }
        }
        return answer;
    }
}