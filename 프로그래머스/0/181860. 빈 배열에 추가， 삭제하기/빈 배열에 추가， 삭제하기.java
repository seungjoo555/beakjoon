import java.util.ArrayList;

class Solution {
    public int[] solution(int[] arr, boolean[] flag) {
        ArrayList<Integer> answerList = new ArrayList<>();
        for(int i = 0; i < arr.length; i++){
            if(flag[i]){
                int t = arr[i] * 2;
                for(int j = 0; j < t; j++){
                    answerList.add(arr[i]);
                }
            } else {
                for(int k = 0; k < arr[i]; k++){
                    answerList.remove(answerList.size() - 1);
                }
            }
        }
        
        int[] answer = answerList.stream().mapToInt(Integer::intValue).toArray();
        return answer;
    }
}