class Solution {
    public String solution(String my_string, int[] indices) {
        char[] str = my_string.toCharArray();
        for (int idx : indices){
            str[idx] = ' ';
        }
        StringBuilder sb = new StringBuilder();
        for (char ch : str){
            if (ch != ' ') sb.append(ch);
        }
        String answer = sb.toString();
        return answer;
    }
}