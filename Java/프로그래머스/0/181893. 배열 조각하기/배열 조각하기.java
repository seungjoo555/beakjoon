import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr, int[] query) {
        for (int i = 0; i< query.length; i++){
            int j = query[i];
            if ((i&1) == 0){
                arr = Arrays.copyOfRange(arr, 0, j+1);
            } else {
                arr = Arrays.copyOfRange(arr, j, arr.length);
            }
        }
        return arr;
    }
}