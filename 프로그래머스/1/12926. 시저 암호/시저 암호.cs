using System.Text;

public class Solution {
    public string solution(string s, int n) {
        string upp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        string low = "abcdefghijklmnopqrstuvwxyz";
        StringBuilder answer = new StringBuilder();
        foreach (char c in s) {
            if (char.IsUpper(c)) {
                answer.Append(upp[(upp.IndexOf(c) + n) % upp.Length]);
            }
            else if (char.IsLower(c)) {
                answer.Append(low[(low.IndexOf(c) + n) % low.Length]);
            }
            else {
                answer.Append(c);
            }
        }
        return answer.ToString();
    }
}