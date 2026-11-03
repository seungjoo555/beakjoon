import java.util.*;

class Solution {
    public String[] solution(String[] strArr) {
        ArrayList<String> strList = new ArrayList<>();
        for(String str : strArr){
            if (!str.contains("ad")){
                strList.add(str);
            }
        }
        String[] answer = new String[strList.size()];
        answer = strList.toArray(new String[0]);
        return answer;
    }
}