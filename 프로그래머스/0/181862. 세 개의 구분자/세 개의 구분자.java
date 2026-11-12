class Solution {
    public String[] solution(String myStr) {
        String[] answer = myStr.replaceFirst("^[abc]+", "").split("[abc]+");
        if (answer[0].equals("")){
            answer[0] = "EMPTY";
        }
        return answer;
    }
}