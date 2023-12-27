import java.util.Arrays;
class Solution {
    public int solution(int a, int b, int c, int d) {
        int answer = 0;
        int NumArr[] = {a, b, c, d};
        Arrays.sort(NumArr);
        
        if(NumArr[0] == NumArr[3]) return 1111 * NumArr[0];
        else if(NumArr[0] == NumArr[2] || NumArr[1] == NumArr[3]) return (int)Math.pow((NumArr[1] * 10)  + NumArr[0] + NumArr[3] - NumArr[1], 2);
        else if(NumArr[0] == NumArr[1] && NumArr[2] == NumArr[3]) return (NumArr[0] + NumArr[3]) * (NumArr[3] - NumArr[0]);
        else if(NumArr[0] == NumArr[1]) return NumArr[2] * NumArr[3];
        else if(NumArr[1] == NumArr[2]) return NumArr[0] * NumArr[3];
        else if(NumArr[2] == NumArr[3]) return NumArr[0] * NumArr[1];
        else return NumArr[0];

    }
}