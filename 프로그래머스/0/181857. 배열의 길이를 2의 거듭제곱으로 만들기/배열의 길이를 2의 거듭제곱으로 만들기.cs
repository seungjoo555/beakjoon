using System;

public class Solution {
    public int[] solution(int[] arr) {
        int l = 1;
        for(int i = 1; i < arr.Length; i *= 2){
            l = i * 2;
        }
        
        int[] answer = new int[l];
        Array.Copy(arr, answer, arr.Length);
        
        return answer;
    }
}