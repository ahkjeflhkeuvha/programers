import java.util.*;
import java.util.stream.*;

class Solution {
    private static final String ENTER_FORMAT = "%s님이 들어왔습니다.";
    private static final String LEAVE_FORMAT = "%s님이 나갔습니다.";

    private void createOrUpdateInfo(Map<String, String> userMap, String messages){
        String userid = messages.split(" ")[1];
        String username = messages.split(" ")[2];
        
        userMap.put(userid, username);
    }
    
    private String formateString(Map<String, String> userMap, String messages){
        String mode = messages.split(" ")[0];
        String userid = messages.split(" ")[1];
        
        if(mode.equals("Enter")) return String.format(ENTER_FORMAT, userMap.get(userid));
        else if(mode.equals("Leave")) return String.format(LEAVE_FORMAT, userMap.get(userid));
        else return "";
    }
    
    public String[] solution(String[] record) {
        Map<String, String> userMap = new HashMap();

        Stream.of(record)
            .filter(o -> o.startsWith("Enter") || o.startsWith("Change")) // Enter나 Change로 시작하는 문자열 찾기
            .forEach(o -> createOrUpdateInfo(userMap, o)); // createOrUpdateInfo로 보내기 
        
        return Stream.of(record)
            .map(o -> formateString(userMap, o))
            .filter(o -> !"".equals(o))
            .toArray(String[]::new);
    }
}