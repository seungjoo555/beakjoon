import java.util.HashMap;

class Solution {
    public String solution(int[] numLog) {
        HashMap<Integer, String> map = new HashMap<>();
        StringBuilder sb = new StringBuilder();
        String answer = "";
        map.put(1, "w");
        map.put(-1, "s");
        map.put(10, "d");
        map.put(-10, "a");
        for (int i = 0; i < (numLog.length-1); i++){
            sb.append(map.get(numLog[i+1] - numLog[i]));
        }
        answer = sb.toString();
        return answer;
    }
}