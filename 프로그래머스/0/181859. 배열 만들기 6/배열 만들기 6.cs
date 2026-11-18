using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int[] arr) {
        Stack<int> stk = new Stack<int>();
        
        for(int i = 0; i < arr.Length; i++){
            if(stk.Count == 0){
                stk.Push(arr[i]);
            }
            else if(stk.Peek() == arr[i]){
                stk.Pop();
            }
            else{
                stk.Push(arr[i]);
            }
        }
        
        int[] answer;
        if(stk.Count == 0){
            answer = new int[]{-1};
        } else {
            answer = stk.ToArray();
            Array.Reverse(answer);
        }
        
        return answer;
    }
}