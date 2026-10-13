import java.util.ArrayList;

class Solution {
    public String[] solution(String[] todo_list, boolean[] finished) {
        ArrayList<String> str = new ArrayList<>();
        for (int i = 0; i < todo_list.length; i++){
            if(!finished[i]){
                str.add(todo_list[i]);
            }
        }
        String[] answer = str.toArray(new String[0]);
        return answer;
    }
}