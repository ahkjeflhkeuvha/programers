class Solution {
    public int[] solution(int[] emergency) {
        int[] answer = new int[emergency.length];
        int max = 0, idx = 0, score = 1, j;
        
        for(int i = 0; i<emergency.length; i++){
            max = 0; idx = 0;
            for(j = 0; j<emergency.length; j++){
                if(emergency[j] > max) {
                    max = emergency[j];
                    idx = j;
                }
            }
            System.out.println(max + "  " + idx);
            answer[idx] = score++;
            emergency[idx] = 0;
        }

        return answer;
    }
}