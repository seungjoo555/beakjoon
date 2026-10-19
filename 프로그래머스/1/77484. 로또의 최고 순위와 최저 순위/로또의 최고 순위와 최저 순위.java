import java.util.Arrays;

class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int zC = 0;
        int shot = 0;
        for(int n : lottos){
            if(n == 0) zC++;
            boolean c = Arrays.stream(win_nums).anyMatch(x -> x == n);
            if(c){
                shot++;
            }
        }
        int high = 7-(shot+zC) == 7 ? 6 : 7-(shot+zC);
        int low = 7-shot == 7 ? 6 : 7-shot;
        int[] answer = new int[]{high, low};
        return answer;
    }
}