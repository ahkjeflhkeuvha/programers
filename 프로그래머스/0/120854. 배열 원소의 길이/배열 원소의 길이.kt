class Solution {
    fun solution(strlist: Array<String>): IntArray {
        var answer: IntArray = IntArray(strlist.size)
        var j:Int = 0
        for(i in strlist) answer[j++] = i.length
        return answer
    }
}