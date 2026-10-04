class Solution {
    public int[] solution(int[] arr, int[][] intervals) {
        int a1 = intervals[0][0], a2 = intervals[0][1], b1 = intervals[1][0], b2 = intervals[1][1];
        int[] answer = new int[(a2+b2+2)-(a1+b1)];
        System.arraycopy(arr, a1, answer, 0, a2-a1+1);
        System.arraycopy(arr, b1, answer, a2-a1+1, b2-b1+1);
        return answer;
    }
}