using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int[] arr) {
        List<int> res = new List<int>();
        foreach(int i in arr){
            for (int j = 0; j < i; j++){
                res.Add(i);
            }
        }
        int[] answer = res.ToArray();
        return answer;
    }
}