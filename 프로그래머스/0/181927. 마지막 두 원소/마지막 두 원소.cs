using System;

public class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[num_list.Length + 1];
        Array.Copy(num_list, answer, num_list.Length);
        if (num_list[^1] > num_list[^2])
            answer[^1] = num_list[^1] - num_list[^2];
        else
            answer[^1] = num_list[^1] * 2;
        return answer;
    }
}