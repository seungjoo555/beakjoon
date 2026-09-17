class Solution {
    public String solution(String my_string, int s, int e) {
        StringBuilder sb = new StringBuilder(my_string);
        StringBuilder temp = new StringBuilder(my_string.substring(s, e+1)).reverse();
        String st = temp.toString();
        sb.replace(s, e+1, st);
        String answer = sb.toString();
        return answer;
    }
}