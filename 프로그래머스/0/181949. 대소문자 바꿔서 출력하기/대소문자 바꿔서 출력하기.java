import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String res = "";
        for(int i = 0; i<a.length(); i++){
            if(a.charAt(i) >= 'a' && a.charAt(i)<='z') res += (char)(a.charAt(i)-32);
            else res += (char)(a.charAt(i)+32);
        }
        System.out.println(res);
    }
}