using System;
using System.Linq;

public class Solution {
    public int solution(string[] strArr) {
        int[] temp = new int[30];
        int answer = 0;
        foreach(string str in strArr){
            temp[str.Length-1] += 1;
        }
        answer = temp.Max();
        return answer;
    }
}