class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        StringBuilder sb = new StringBuilder();
        for(char ch : myString.toCharArray()){
            if(ch == 'A'){
                sb.append("B");
            } else {
                sb.append("A");
            }
        }
        if (sb.indexOf(pat) != -1){
            answer = 1;
        }
        return answer;
    }
}