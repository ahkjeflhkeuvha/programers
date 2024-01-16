import java.util.*;
import java.util.stream.Collectors;
class Solution {
    public int solution(int[] array) {
        return (int)Arrays.stream(Arrays.stream(array).mapToObj(String::valueOf).collect(Collectors.joining()).split("")).filter(str -> str.equals("7")).count();
    }
}