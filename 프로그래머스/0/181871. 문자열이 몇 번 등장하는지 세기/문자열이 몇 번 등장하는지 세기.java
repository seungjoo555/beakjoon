class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        int msl = myString.length();
        int pl = pat.length();
        for (int i = 0; i <= msl - pl; i++){
            if (myString.substring(i, i+pl).equals(pat)){
                answer++;
            }
        }
        return answer;
    }
}