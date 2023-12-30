class Solution {
    public int solution(int[] array) {
        int answer = 0;
        int maxArr[] = new int[1000], max = 0;
        for(int i = 0; i<array.length; i++){
            maxArr[array[i]]++;
            if(maxArr[array[i]] > max) {
                max = maxArr[array[i]];
                answer = array[i];
            }
        }
        int temp = 0;
        for(int i = 0; i<maxArr.length; i++){
            if(maxArr[i] == max) temp++;
            if(temp > 1) answer = -1;
        }

        return answer;
    }
}