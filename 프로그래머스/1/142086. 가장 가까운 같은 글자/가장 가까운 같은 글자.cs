using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] solution(string s) {
        Dictionary<string, int> word = new Dictionary<string, int>();
        List<int> result = new List<int>();
        foreach (char c in s) {
            foreach (var key in word.Keys.ToList()) {
                word[key] += 1;
            }
            string ch = c.ToString();
            if (word.ContainsKey(ch)) {
                result.Add(word[ch]);
                word[ch] = 0;
            }
            else {
                result.Add(-1);
                word.Add(ch, 0);
            }
        }
        int[] answer = result.ToArray();
        return answer;
    }
}