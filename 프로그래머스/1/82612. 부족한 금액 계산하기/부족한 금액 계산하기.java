import java.util.*;
class Solution {
    public long solution(int price, int money, int count) {
        long answer = money;
        
        answer -= (long) price*(count*(count+1))/2;
        if (answer < 0){
            answer = -answer;
        }else{
            answer = 0;
        }
        
        return answer;
    }
}