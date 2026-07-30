using System;

public class Solution {
    public int solution(int n, string control) {
        int answer = n;
        foreach (char ch in control){
            switch (ch){
                case 'w':
                    answer += 1;
                    break;
                case 's':
                    answer -= 1;
                    break;
                case 'd':
                    answer += 10;
                    break;
                case 'a':
                    answer -= 10;
                    break;
                default:
                    break;
            }
        }
        return answer;
    }
}