using System;
using System.Linq;

public class Solution {
    public int[] solution(int[] array) {
        int max = array.Max();
        int[] answer = new int[] {max, Array.IndexOf(array, max)};
        return answer;
    }
}