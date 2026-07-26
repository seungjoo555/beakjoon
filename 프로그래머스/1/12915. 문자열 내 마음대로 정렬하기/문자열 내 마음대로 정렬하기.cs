using System;
public class Solution {
    public string[] solution(string[] strings, int n) {
        Array.Sort(strings, (a, b) => {
            if (a[n] != b[n])
                return a[n].CompareTo(b[n]);
            return a.CompareTo(b);
        });
        return strings;
    }
}