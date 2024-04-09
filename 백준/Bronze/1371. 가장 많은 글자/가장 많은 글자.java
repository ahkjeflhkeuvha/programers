import java.util.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args){
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input;
		String str = "";
		while((input = br.readLine()) != null) {
			str += input;
		}
        int strArr[] = new int[26];
        
        int max = 0;
        
        for(int i = 0; i<str.length(); i++) {
        	if(str.charAt(i) == ' ') continue;
        	strArr[str.charAt(i) - 'a']++;
        }
        
        for(int i = 0; i<strArr.length; i++) {
        	if(strArr[i] > max) max = strArr[i];
        }
        for(int i = 0; i<strArr.length; i++) {
        	if(strArr[i] == max) System.out.print((char)(i + 'a'));
        }
        }
        catch (Exception e    ){
            System.out.println("에러~");
        }
	}
}


