import java.util.*;
class Solution {
    public String[] solution(String[] record) {
        ArrayList<String> list = new ArrayList<>();
        HashMap<String, String> map = new HashMap<>();
        
        for(int i = 0; i<record.length; i++){
            String strArr[] = record[i].split(" ");
            
            if(strArr[0].equals("Leave")) continue;
            else map.put(strArr[1], strArr[2]);
        }
        // System.out.println(map);
        
        for(int i = 0, j = 0; i<record.length; i++){
            String strArr[] = record[i].split(" ");
            
            if(strArr[0].equals("Leave")) list.add(map.get(strArr[1]) + "님이 나갔습니다.");
            else if (strArr[0].equals("Enter")) list.add(map.get(strArr[1]) + "님이 들어왔습니다.");
        }
        
        // System.out.println(list);
        String answer[] = new String[list.size()];
        int i = 0;
        for(String str : list){
            answer[i++] = str;
        }
        return answer;
    }
}