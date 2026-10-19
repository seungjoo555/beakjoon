class Solution {
    public int solution(String[][] board, int h, int w) {
        int answer = 0;
        int[] dh = {0, 1, -1, 0};
        int[] dw = {1, 0, 0, -1};
        for(int i = 0; i < 4; i++){
            int hc = h + dh[i];
            int wc = w + dw[i];
            if ((hc >= 0 && hc < board.length) && (wc >= 0 && wc < board.length)){
                if(board[h][w].equals(board[hc][wc])){
                    answer++;
                }
            }
        }
        return answer;
    }
}