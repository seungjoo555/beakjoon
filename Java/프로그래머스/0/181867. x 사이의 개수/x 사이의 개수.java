import java.util.ArrayList;

class Solution {
    public int[] solution(String myString) {
        ArrayList<Integer> res = new ArrayList<>();
        int count = 0;
        for(char ch: myString.toCharArray()){
            if(ch == 'x'){
                res.add(count);
                count = 0;
            } else {
                count++;
            }
        }
        res.add(count);
        int[] answer = new int[res.size()];
        for(int i = 0; i < res.size(); i++){
            answer[i] = res.get(i);
        }
        return answer;
    }
}