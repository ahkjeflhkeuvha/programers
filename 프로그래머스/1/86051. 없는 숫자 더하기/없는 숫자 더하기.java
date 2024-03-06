class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        String str = "0123456789";
        
        for(int i = 0; i<numbers.length; i++){
            if(str.contains(Integer.toString(numbers[i]))) answer += numbers[i];
        }
        return 45 - answer;
    }
}