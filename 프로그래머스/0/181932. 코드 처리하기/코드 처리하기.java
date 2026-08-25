class Solution {
    public String solution(String code) {
        String answer = "";
        StringBuilder sb = new StringBuilder("");
        int mode = 0;
        for (int i = 0; i < code.length(); i++) {
            char ch = code.charAt(i);
            if (ch == '1') {
                mode ^= 1;
            } else {
                if (mode == 0) {
                    if ((i & 1) != 1) {
                        sb.append(ch);
                        }
                } else {
                    if ((i & 1) == 1) {
                        sb.append(ch);
                    }
                }
            }
        }
        answer = sb.toString() != "" ? sb.toString(): "EMPTY";
        return answer;
    }
}