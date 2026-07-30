using System;
using System.Linq;

public class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int sum = num_list.Sum();
        int mul = num_list.Aggregate(1, (acc, next) => acc * next);
        if ((sum*sum) > mul)
            answer = 1;
        else
            answer = 0;
        return answer;
    }
}