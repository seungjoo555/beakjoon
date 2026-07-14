using System;

public class Solution {
    public int solution(int[] num_list) {
        String odd = "";
        String even = "";
        foreach (int i in num_list){
            if ((i & 1) == 1)
                odd += i.ToString();
            else
                even += i.ToString();
        }
        int answer = int.Parse(odd) + int.Parse(even);
        return answer;
    }
}