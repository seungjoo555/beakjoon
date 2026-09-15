import java.util.Arrays;

class Solution {
    public int solution(String my_string, String is_prefix) {
        int answer = 0;
        int l = my_string.length();
        String[] jub = new String[l];
        for(int i = 0; i < l; i++){
            jub[i] = my_string.substring(0, i+1);
        }
        if (Arrays.asList(jub).contains(is_prefix)) answer = 1;
        
        return answer;
    }
}