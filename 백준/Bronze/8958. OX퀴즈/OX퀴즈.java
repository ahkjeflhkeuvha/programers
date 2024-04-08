import java.util.*;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int len = sc.nextInt();
        
        String str[] = new String[len];
        for(int i = 0; i<len; i++){
            str[i] = sc.next();
        }
		
        for(int i = 0; i<str.length; i++) {
            int sum = 0, num = 0, n = 1;
            String strArr[] = str[i].split("");
            
            for(int j = 0; j<strArr.length; j++) {
			    num = 0;
			    if(strArr[j].equals("O")) {
				    num += n;
				    n++;
			       }
			    else n = 1;
			    sum += num;
		    }
            System.out.println(sum);
        }
	}
}