using System;

public class Solution {
    public int[] solution(int[] num_list) {
        Array.Sort(num_list);
        int[] answer = num_list[5..^0];
        return answer;
    }
}