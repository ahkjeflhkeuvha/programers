import java.util.*;
class Solution {
    public String solution(String polynomial) {
        int numX = 0, num = 0;
        String strArr[] = polynomial.split(" ");
    
        for(int i = 0; i<strArr.length; i++){
            if(strArr[i].equals("+")) continue;
            else if(strArr[i].contains("x")){
                if(strArr[i].equals("x")) numX++;
                else numX += Integer.parseInt(strArr[i].split("x")[0]);
            }
            else num += Integer.parseInt(strArr[i]);
        }
        
        if(numX == 0) {
            if(num == 0) return 0 + "";
            else return num + "";
        }
        else if(numX == 1){
            if(num == 0) return "x";
            else return "x + " + num;
        }
        else {
            if(num == 0) return numX + "x";
            else return numX + "x + " + num;
        }
        
    }
}