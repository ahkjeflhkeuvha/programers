class Solution {
    fun solution(sides: IntArray): Int {
        return sides.sorted().let{(x, y, z) -> if (x+y > z) 1 else 2}
    }
}