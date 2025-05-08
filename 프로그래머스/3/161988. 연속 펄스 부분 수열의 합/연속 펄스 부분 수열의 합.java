import java.util.*;
class Solution {
    public long solution(int[] sequence) {
        long answer = 0;
        long max1 = 0;
        long max2 = 0;
        long dp1 = 0;
        long dp2 = 0;
        for(int i=0;i<sequence.length;i++){
            int val = sequence[i];
            int p1 = i%2==0 ? 1:-1;
            int p2 = -p1;
            dp1 = Math.max(val*p1, dp1+val*p1);
            dp2 = Math.max(val*p2, dp2+val*p2);
            
            max1 = Math.max(dp1, max1);
            max2 = Math.max(dp2, max2);
        }
        
        
        return Math.max(max1,max2);
    }
}