class Solution {
    public int[] solution(int start_num, int end_num) {
        int t = start_num - end_num + 1;
        int[] answer = new int[t];
        for (int i = 0; i < t; i++){
            answer[i] = start_num--;
        }
        return answer;
    }
}