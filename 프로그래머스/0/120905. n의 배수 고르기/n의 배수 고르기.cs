using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int n, int[] numlist) {
        List<int> temp = new List<int>();
        foreach(int i in numlist){
            if(i % n == 0){
                temp.Add(i);
            }
        }
        int[] answer = temp.ToArray();
        return answer;
    }
}