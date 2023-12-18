class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        String before = my_string.substring(0, s);
        String after = my_string.substring(overwrite_string.length() + s);
        return before + overwrite_string + after;
    }
}