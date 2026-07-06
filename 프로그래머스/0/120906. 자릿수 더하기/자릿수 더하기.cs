using System;
using System.Linq;
public class Solution {
    public int solution(int n) {
        int answer = n.ToString().Select(s => s - '0').Sum();
        return answer;
    }
}