public class Solution {
    public string solution(string s, int n) {
        string upp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        string low = "abcdefghijklmnopqrstuvwxyz";
        string answer = "";
        foreach(char c in s) {
            if (char.IsUpper(c)) {
                answer += upp[(upp.IndexOf(c) + n) % upp.Length];
            }
            else if (char.IsLower(c)) {
                answer += low[(low.IndexOf(c) + n) % low.Length];
            }
            else {
                answer += " ";
            }
        }
        return answer;
    }
}