class Solution {
    public String[] solution(String[] str_list) {
        String[] answer = null;
        int n = -1;
        for (int i = 0; i < str_list.length; i++){
            if (str_list[i].equals("l") || str_list[i].equals("r")){
                n = i;
                break;
            }
        }
        if (n == -1){
            answer = new String[0];
        } else if (str_list[n].equals("l")){
            answer = new String[n];
            if (n != 0) {
            	System.arraycopy(str_list, 0, answer, 0, n);            	
            }
        } else if (str_list[n].equals("r")) {
        	answer = new String[str_list.length - (n + 1)];
        	if (str_list.length - (n + 1) != 0) {
        		System.arraycopy(str_list, n + 1, answer, 0, str_list.length - (n + 1));        	        		
        	}
        }
        return answer;
    }
}