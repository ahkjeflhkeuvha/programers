class Solution {
    fun solution(slice: Int, n: Int): Int {
        var answer: Int = 0
        var sliceNum: Int = 0
        while(sliceNum < n){
            sliceNum += slice
            answer++
        }
        return answer
    }
}