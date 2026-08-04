using System;
using System.Text;

public class Solution {
    public string solution(string[] str_list, string ex) {
        StringBuilder answer = new StringBuilder();
        foreach(string st in str_list){
            if (!st.Contains(ex))
                answer.Append(st);
        }
        string res = answer.ToString();
        return res;
    }
}