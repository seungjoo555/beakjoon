import java.util.Arrays;
import java.util.stream.IntStream;

class Solution {
    public int[] solution(int n, int[] slicer, int[] num_list) {
        int[] answer = null;
        if (n == 1){
            answer = Arrays.copyOfRange(num_list, 0, slicer[1]+1);
        } else if (n == 2){
            answer = Arrays.copyOfRange(num_list, slicer[0], num_list.length);
        } else if (n == 3){
            answer = Arrays.copyOfRange(num_list, slicer[0], slicer[1]+1);
        } else if (n == 4){
            answer = IntStream.rangeClosed(slicer[0], slicer[1])
                .filter(i -> (i-slicer[0]) % slicer[2] == 0)
                .map(i -> num_list[i])
                .toArray();
        }
        return answer;
    }
}