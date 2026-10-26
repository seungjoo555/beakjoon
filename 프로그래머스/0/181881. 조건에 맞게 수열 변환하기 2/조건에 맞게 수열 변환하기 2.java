import java.util.Arrays;

class Solution {
    public int solution(int[] arr) {
        
        int answer = 0;
        int [] arr2 = new int[arr.length];
        System.arraycopy(arr, 0, arr2, 0, arr.length);
        
        while(true){
            for(int i = 0; i < arr.length; i++){
                if(arr[i] >= 50 && (arr[i] & 1) == 0){
                    arr2[i] = arr[i] / 2;
                } else if(arr[i] < 50 && (arr[i] & 1) == 1) {
                    arr2[i] = arr[i] * 2 + 1;
                }
            }

            if(Arrays.equals(arr, arr2)){
                break;
            } else {
                System.arraycopy(arr2, 0, arr, 0, arr2.length);
                answer++;
            }
        }
        
        return answer;
    }
}