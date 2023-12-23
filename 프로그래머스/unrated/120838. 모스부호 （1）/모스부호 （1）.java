class Solution {
    public String solution(String letter) {
        String answer = "";
        String[] morse = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        String[] morseVal = letter.split(" ");
        
        for(int i = 0; i<morseVal.length; i++){
            for(int j = 0; j<morse.length; j++){
                if(morseVal[i].equals(morse[j])) answer += (char)(j + 97);
            }
        }
        
        return answer;
    }
}