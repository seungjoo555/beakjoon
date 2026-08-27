import java.util.stream.Stream;

class Solution {
    public int solution(int a, int b, int c) {
        int answer = 0;
        long count = Stream.of(a, b, c).distinct().count();
        switch((int)count){
            case 1:
                answer = (a + b + c) * (a*a + b*b + c*c) * (a*a*a + b*b*b + c*c*c);
                break;
            case 2:
                answer = (a + b + c) * (a*a + b*b + c*c);
                break;
            case 3:
                answer = (a + b + c);
                break;
        }
        
        return answer;
    }
}