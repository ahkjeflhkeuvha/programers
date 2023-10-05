class Solution {
    public int solution(int[] array) {
        int answer = 0, temp = 0;
        int ans_arr[] = new int[array.length];
        
        for(int i = 0; i<array.length; i++){
            for(int j = 0; j<array.length; j++){
                if(array[i] < array[j]) {
                    temp = array[i];
                    array[i] = array[j];
                    array[j] = temp;
                }
            }
        }
        // 배열을 오름차순으로 바꾸는 코드
        
        // for(int i = 0; i<array.length; i++){
        //     for(int j = 0; j<array.length; j++){
        //         if(array[i] > array[j]){
        //             temp = array[i];
        //             array[i] = array[j];
        //             array[j] = temp;
        //         }
        //     }
        // }
        
        return answer = array[array.length/2];
    }
}