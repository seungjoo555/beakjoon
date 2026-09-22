class Solution {
    public int[] solution(String my_string) {
        int[] answer = new int[52];
        
        for (int i = 0; i < my_string.length(); i++){
            int j = (int)my_string.charAt(i)-65;
            j = (j > 25) ? j-6 : j;
            answer[j] += 1;
        }
        
        return answer;
    }
}