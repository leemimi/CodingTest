import java.util.*;
class Solution {
    static int n;
    public long solution(int cap, int n, int[] deliveries, int[] pickups) {
        long answer = 0;
        n = deliveries.length;
        
        int arrive = 0;
        int pick = 0;
        
        for(int i=deliveries.length-1; i>-1;i--){
            int cnt = 0;
            arrive -= deliveries[i];
            pick -= pickups[i];
            while(arrive<0 || pick<0){
                arrive += cap;
                pick += cap;
                cnt++;
            }
            answer += (i+1)*2*cnt;

        }

        
        return answer;
    }
}