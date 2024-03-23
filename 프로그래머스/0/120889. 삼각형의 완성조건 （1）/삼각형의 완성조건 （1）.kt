class Solution {
    fun solution(sides: IntArray): Int {
        val arr = sides.sorted()
        // println("${sides[0]} ${sides[1]} ${sides[2]}")
        if(arr[0] + arr[1] > arr[2]) return 1
        else return 2
    }
}