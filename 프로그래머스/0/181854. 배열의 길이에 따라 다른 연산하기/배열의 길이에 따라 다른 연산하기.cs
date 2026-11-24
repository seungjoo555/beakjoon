using System;

public class Solution {
    public int[] solution(int[] arr, int n) {
        if((arr.Length & 1) == 0){
            for(int i = 1; i < arr.Length; i += 2){
                arr[i] += n;
            }
        } else {
            for(int j = 0; j < arr.Length; j += 2){
                arr[j] += n;
            }
        }
        return arr;
    }
}