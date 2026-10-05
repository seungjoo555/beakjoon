class Solution {
    public int[] solution(int[] arr) {
        int min = -1;
        int max = -1;
        for (int i = 0; i < arr.length; i++){
            if (arr[i] == 2){
                min = i;
                break;
            }
        }
        if (min != -1){
            for (int i = arr.length-1; i >= 0; i--){
                if (arr[i] == 2){
                    max = i;
                    break;
                }
            }
        }
        int[] answer = new int[max-min+1];
        if (min == -1){
            answer[0] = -1;
        } else if (min == max){
            answer[0] = 2;
        } else {
            System.arraycopy(arr, min, answer, 0, max-min+1);
        }
        return answer;
    }
}