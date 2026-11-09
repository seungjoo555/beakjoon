import java.util.Arrays;

class Solution {
    public int solution(String binomial) {
        int answer = 0;
        String[] t = binomial.split(" ");
        if (t[1].equals("+")) {
            answer = Integer.parseInt(t[0]) + Integer.parseInt(t[2]);
        } else if (t[1].equals("-")) {
            answer = Integer.parseInt(t[0]) - Integer.parseInt(t[2]);
        } else if (t[1].equals("*")) {
            answer = Integer.parseInt(t[0]) * Integer.parseInt(t[2]);
        }
        return answer;
    }
}