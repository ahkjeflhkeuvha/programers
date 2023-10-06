class Solution {
    public int solution(int order) {
        int answer = 0, sum = 0;
        String st = Integer.toString(order);
        
        for(int i = 0; i<st.length(); i++){
            if((st.charAt(i) - 48)%3 == 0){
                if((st.charAt(i)-48) == 0) continue;
                sum++;
            }
            System.out.println(st.charAt(i)-48);
        }
        return answer = sum;
    }
}