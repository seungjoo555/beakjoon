using System;
using System.Linq;

public class Solution {
    public int solution(int n) {
        return (n & 1) == 1
            ? Enumerable.Range(1, n).Where(i => (i & 1) == 1).Sum()
            : Enumerable.Range(1, n).Where(i => (i & 1) == 0).Select(i => i * i).Sum();
    }
}