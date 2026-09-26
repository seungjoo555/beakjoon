class Solution {
    public int[] solution(int n, int k) {
        int t = n/k;
        int s = k;
        int[] answer = new int[t];
        for (int i = 0; i < t; i++){
            answer[i] = s;
            s += k;
        }
        return answer;
    }
}