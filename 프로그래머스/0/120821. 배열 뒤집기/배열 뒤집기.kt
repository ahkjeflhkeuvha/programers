class Solution {
    fun solution(num_list: IntArray): IntArray {
        var answer = IntArray(num_list.size){0}
        var j = 0
        for(i in num_list.reversed()) answer[j++] = i
        return answer
    }
}