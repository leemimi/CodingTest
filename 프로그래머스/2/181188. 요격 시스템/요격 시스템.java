import java.util.*;
class Solution {
    public int solution(int[][] targets) {
        int answer = 1;
        Arrays.sort(targets, (a,b)->Integer.compare(a[1],b[1]));

        int prev = targets[0][1];
        for(int[]ta: targets){
            if(prev <= ta[0]){
                answer++;
                prev = ta[1];
                System.out.println(ta[0]);
            }
        }
        
        
        return answer;
    }
}