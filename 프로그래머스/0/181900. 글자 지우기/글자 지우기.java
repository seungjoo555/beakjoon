import java.util.ArrayList;
import java.util.Arrays;
import java.util.stream.Collectors;

class Solution {
    public String solution(String my_string, int[] indices) {
        StringBuilder sb = new StringBuilder();
        ArrayList<Integer> nIndices = 
            Arrays.stream(indices).boxed().collect(Collectors.toCollection(ArrayList::new));
        for (int i = 0; i < my_string.length(); i++){
            if (nIndices.contains(i)) continue;
            sb.append(my_string.charAt(i));
        }
        String answer = sb.toString();
        return answer;
    }
}