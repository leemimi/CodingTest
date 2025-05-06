import java.util.*;
class Solution {
    public int[] solution(int n, int s) {
        int[] answer = new int[n];
        
        if(s<n) return new int[]{-1};
        
        int a = s/n;
        int b = s%n;
        
        Arrays.fill(answer, a);
        for(int i=n-1;i>=n-b;i--){
            answer[i]++;
        }
        
        
        return answer;
    }
}