class Solution {
    fun solution(slice: Int, n: Int): Int {
        var answer: Int = 0
        var sliceNum: Int = 0
        while(true){
            if(sliceNum >= n) break;
            sliceNum += slice
            answer++
        }
        return answer
    }
}