import java.util.*;
class Solution {
    public int solution(int n) {
        int answer = n+1;
        
        int num = Integer.bitCount(n);
        
        while(true){
            n++;
            int next = Integer.bitCount(n);
            if(num == next){
                break;
            }
            answer++;
        }
        return answer;
    }
}