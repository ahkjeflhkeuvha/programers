class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        String str;
        for(int i = 0; i<n; i++){
            str = String.format("%16s", Integer.toBinaryString(arr1[i] | arr2[i]));
            str = str.substring(str.length() - n);
            str = str.replaceAll("1", "#").replaceAll("0", " ");
            answer[i] = str;
        }
        return answer;
    }
}