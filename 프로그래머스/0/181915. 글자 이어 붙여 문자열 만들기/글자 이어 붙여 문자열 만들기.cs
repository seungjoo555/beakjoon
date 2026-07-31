using System;
using System.Collections.Generic;

public class Solution {
    public string solution(string my_string, int[] index_list) {
        string answer = "";
        List<char> temp = new List<char>();
        foreach (int i in index_list) {
            temp.Add(my_string[i]);
        }
        answer = String.Join("", temp);
        return answer;
    }
}