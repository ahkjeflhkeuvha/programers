import java.math.BigInteger;
class Solution {
    public String solution(String a, String b) {
        BigInteger BigA = new BigInteger(a);
        BigInteger BigB = new BigInteger(b);
        BigInteger sum = BigA.add(BigB);
        return sum.toString();
    }
}