using System;
using System.Linq;

public class Solution {
    public int[] solution(int[] arr, int k) {
        int[] answer = new int[k];
        int[] temp = arr.Distinct().ToArray();
        for(int i = 0; i < k; i++){
            if(i < temp.Length){
                answer[i] = temp[i];
            } else {
                answer[i] = -1;
            }
        }
        return answer;
    }
}