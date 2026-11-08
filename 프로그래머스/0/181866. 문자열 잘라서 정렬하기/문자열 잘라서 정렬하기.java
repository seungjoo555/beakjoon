import java.util.Arrays;

class Solution {
    public String[] solution(String myString) {
        String myString2 = myString.replaceAll("^x+", "");
        String[] answer = myString2.split("x+");
        Arrays.sort(answer);
        return answer;
    }
}