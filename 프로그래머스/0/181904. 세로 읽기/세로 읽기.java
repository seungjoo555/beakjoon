class Solution {
    public String solution(String my_string, int m, int c) {
        StringBuilder sb = new StringBuilder();
        
        for (int i = c; i < my_string.length()+1; i+=m){
            sb.append(my_string.charAt(i-1));
        }
        
        String answer = sb.toString();
        return answer;
    }
}