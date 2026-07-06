using System;

public class Solution {
    public int solution(string[] s1, string[] s2) {
        int answer = 0;
        foreach(string s in s1){
            if (Array.Exists(s2, w => w == s)){
                answer += 1;
            }
        }
        return answer;
    }
}